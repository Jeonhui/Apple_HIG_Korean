June 21, 2023

 Updated to include guidance for visionOS. File management
===============

Depending on the experience, people may expect to manage their documents and files within an app or throughout the system.![A sketch of a document with the upper right corner folded in, suggesting interaction with files. The image is overlaid with rectangular and circular grid lines and is tinted orange to subtly reflect the orange in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/c753c4f8870e5c729becf174c1f0c5e5/patterns-file-management-intro@2x.png)

Document-based apps — such as Pages, Keynote, Photos, and Notes — help people create, edit, and save documents and files, often providing customized ways for people to browse for content they want to open in the app.

Depending on the platform, people may also expect to browse files without first opening an app. On a Mac, people use the Finder to access the macOS file system; on iPhone, iPad, and Apple Vision Pro, people use the Files app to manage the documents and files on their device. In watchOS and tvOS, people don’t typically create, edit, and manage documents.

[Opening files](/design/human-interface-guidelines/file-management#Opening-files)
---------------------------------------------------------------------------------

People are familiar with the system apps and interfaces for browsing and opening files, so it can work well to leverage these experiences in your app.

**Use app menus and keyboard shortcuts to give people convenient ways to create and open documents.** In macOS and iPadOS, people expect to create new documents or open existing ones. When you provide menu commands like New or Open, macOS presents them in the menu bar File menu, and iPadOS presents them in the shortcuts interface that displays when people hold the Command key on a connected hardware keyboard. In contrast, iOS and visionOS don’t display app-level menus in these ways, so it often works well to use an Add (+) button to offer a “new document” action.

**Reflect people’s view of the file system within a custom file-opening interface.** If people already understand the basic layout of their device’s file system — for example, through their use of apps like the Finder and Files — it’s a good idea to build on this understanding in a custom file-opening view. Although it can make sense to start by showing one part of the file system within your custom interface, such as a Documents or iCloud folder or the most recently selected location, avoid forcing people to remain within this area if they want to browse elsewhere.

**Make your custom file-opening interface convenient.** For example, people might appreciate an “open recent” action in addition to the simple “open” action. You might also want to let people choose criteria on which to filter the file-browsing experience, or select multiple documents to open at once. In a macOS open panel, you can customize the title of the Open button to reflect the task — for example, if your app lets people insert a file’s contents into the current document, you might change the title to *Insert*.

[Saving work](/design/human-interface-guidelines/file-management#Saving-work)
-----------------------------------------------------------------------------

**Help people be confident that their work is always preserved unless they cancel or delete it.** In general, avoid making people take an explicit action to save their work. Instead, automatically perform periodic saves while they’re editing and when they close a file or switch to another app.

**Provide a save interface to let people change a file’s name, format, or location.** By default, a new document’s title is “Untitled” until people choose a custom name. As with a document-opening interface, a save view can also provide a browsing experience that defaults to a logical location to help people place the saved document where they want. If you support saving content in different formats, also give people a way to choose a specific file format.

**Hide the file extension by default, but let people view it if they choose.** Be sure to reflect the current choice in all the save or open interfaces you display.

**Extend the functionality of the Save dialog, if appropriate.** If it makes sense in your app, you can add a custom accessory view containing useful settings or options to the Save dialog. For example, the dialog for saving Mail messages as files contains an option to include attachments.

[Quick Look previews](/design/human-interface-guidelines/file-management#Quick-Look-previews)
---------------------------------------------------------------------------------------------

Quick Look helps you create previews of the files your app handles so that people can view them within your app and in some cases interact with them. On a Mac, for example, people can play the preview of an audio file; in iOS, people can add markup to a photo’s preview; and in visionOS, people can rotate and scale a file to examine it in different ways.

**Implement a Quick Look viewer in your app if it makes sense.** If your app lets people attach or otherwise interact with files — especially files your app doesn’t natively support — implementing a Quick Look viewer lets people preview those files without leaving your app.

**Consider implementing a Quick Look generator if your app produces custom file types.** A Quick Look generator lets other apps — including Finder, Files, and Spotlight — display previews of your documents, making it easier for people to find them.

[Platform considerations](/design/human-interface-guidelines/file-management#Platform-considerations)
-----------------------------------------------------------------------------------------------------

*No additional considerations for tvOS, visionOS, or watchOS.*

### [iOS, iPadOS](/design/human-interface-guidelines/file-management#iOS-iPadOS)

If it makes sense for your app to share its files with other apps, you can create a file provider app extension that displays a custom interface for importing, exporting, opening, and moving your app’s documents. For developer guidance, see [File Provider](/documentation/fileprovider)
. An *app extension* is code you provide that people can install and use to extend the functionality of a specific area of the system; to learn more, see [App extensions](https://developer.apple.com/app-extensions/)
.

**When someone uses your file provider extension to open or import documents, display only documents that are appropriate in the current context.** For example, if a PDF-editing app loads your extension, only list PDF files for opening or import. You might also want to display additional information, such as modification dates, sizes, and whether documents are local or remote.

**Let people select a destination when exporting and moving documents.** Unless your app stores documents in a single directory, let people navigate to a specific destination in your directory hierarchy. If it makes sense, you can also provide a way to add new subdirectories.

**Avoid including a custom navigation bar.** Your extension loads within a modal view that already includes a navigation bar. Providing a second navigation bar is confusing and takes space away from your content.

Your app can also let people browse and open files from other apps. For developer guidance, see [Adding a document browser to your app](/documentation/uikit/view_controllers/adding_a_document_browser_to_your_app)
.

### [macOS](/design/human-interface-guidelines/file-management#macOS)

#### [Finder Sync extensions](/design/human-interface-guidelines/file-management#Finder-Sync-extensions)

If your app syncs local and remote files, you can create a Finder Sync app extension to express file synchronization status and control within the Finder. For developer guidance, see [Finder Sync](/documentation/findersync)
.

For example, you can use a Finder Sync extension to:

* Display badges in the Finder to indicate the sync status of items
* Provide custom contextual menu items that perform file and folder management tasks, like favoriting and adding password-protection
* Provide custom toolbar buttons that perform global actions, like initiating a sync operation

**Help people avoid losing work if they turn off autosaving.** People can turn off autosaving by selecting the “Ask to keep changes when closing documents” checkbox in the General system settings pane. In this scenario, show that a document has unsaved changes and present a save dialog when people choose to close the document, quit your app, log out, or restart.

**When autosaving is off, make sure people know when a document has unsaved changes.** To show that there are unsaved changes, display a dot on the document window’s close button and next to the document’s name in your app’s Window menu. When autosaving is on, showing a dot in these locations is confusing, because it implies that people need to take action to avoid losing their work. Regardless of autosave status, you can append “Edited” to the document’s title in the title bar, but be sure to remove this suffix as soon as autosave occurs or when people explicitly save their work.

[Resources](/design/human-interface-guidelines/file-management#Resources)
-------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/file-management#Related)

[Toolbars](/design/human-interface-guidelines/toolbars)


[File menu](/design/human-interface-guidelines/the-menu-bar#File-menu)


[Printing](/design/human-interface-guidelines/printing)


#### [Developer documentation](/design/human-interface-guidelines/file-management#Developer-documentation)

[Documents](/documentation/SwiftUI/Documents)


#### [Videos](/design/human-interface-guidelines/file-management#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/49/68960E87-E488-40C3-90E3-A820B5119FF0/3727_wide_250x141_1x.jpg) Build document-based apps in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10039) 
[Change log](/design/human-interface-guidelines/file-management#Change-log)
---------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |

