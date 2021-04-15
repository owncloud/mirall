Feature: Syncing files

    As a user
    I want to be able to sync my local folders to to my owncloud server
    so that I dont have to upload and download files manually

    Scenario: Syncing a file to the server
        Given user "Alice" has been created on the server with default attributes
		And user "Alice" has set up a client with poll interval settings and password "1234"
        When the user creates a file "lorem-for-upload.txt" with the following content on the file system
            """
            test content
            """
        And the user waits for file "lorem-for-upload.txt" to be synced
        Then as "Alice" the file "lorem-for-upload.txt" on the server should have the content "test content"

    Scenario: Syncing a file from the server
        Given user "Alice" has been created on the server with default attributes
		And user "Alice" has set up a client with poll interval settings and password "1234"
        And user "Alice" has uploaded file on the server with content "test content" to "uploaded-lorem.txt"
        When the user waits for file "uploaded-lorem.txt" to be synced
        Then the file "uploaded-lorem.txt" should exist on the file system with the following content
            """
            test content
            """

    Scenario: Syncing a file from the server and creating a conflict
        Given user "Alice" has been created on the server with default attributes
		And user "Alice" has set up a client with poll interval settings and password "1234"
        And user "Alice" has uploaded file on the server with content "test content" to "uploaded-lorem.txt"
        And the user has waited for file "conflict.txt" to be synced
        And the user has paused the file sync
        And the user has changed the content of local file "conflict.txt" to:
            """
            client content
            """
        And user "Alice" has uploaded file on the server with content "server content" to "uploaded-lorem.txt"
        When the user resumes the file sync on the client
        And the user clicks on the activity tab
        And the user selects the unsynced files tab with 1 unsynced files
        # Then a conflict warning should be shown for 1 files
        Then the table of conflict warnings should include file "conflict.txt"
        And the file "conflict.txt" should exist on the file system with the following content
            """
            server content
            """
        And a conflict file for "conflict.txt" should exist on the file system with the following content
            """
            client content
            """