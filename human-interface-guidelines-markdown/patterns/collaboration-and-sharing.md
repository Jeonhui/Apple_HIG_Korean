June 21, 2023

 Updated to include guidance for visionOS. Collaboration and sharing
=========================

Great collaboration and sharing experiences are simple and responsive, letting people focus on the content while communicating effectively with others.![A sketch of a person with an overlapping checkmark, suggesting effective collaboration. The image is overlaid with rectangular and circular grid lines and is tinted orange to subtly reflect the orange in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/ff23fbfe77df77f6bd5dd710a474b15b/patterns-collaboration-and-sharing-intro@2x.png)

System interfaces and the Messages app can help you provide consistent and convenient ways for people to collaborate and share. For example, people can share content or begin a collaboration by dropping a document into a Messages conversation or selecting a destination in the familiar share sheet.

After a collaboration begins, people can use the collaboration button in your app to communicate with others, perform custom actions, and manage details. In addition, people can receive Messages notifications when collaborators mention them, make changes, join, or leave.

You can take advantage of Messages integration and the system-provided sharing interfaces whether you implement collaboration and sharing through CloudKit, iCloud Drive, or a custom solution. To offer these features when you use a custom collaboration infrastructure, make sure your app also supports universal links (for developer guidance, see [Supporting universal links in your app](/documentation/Xcode/supporting-universal-links-in-your-app)
).

In addition to helping people share and collaborate on documents, visionOS supports immersive sharing experiences through SharePlay. For guidance, see [SharePlay](/design/human-interface-guidelines/shareplay)
.

[Best practices](/design/human-interface-guidelines/collaboration-and-sharing#Best-practices)
---------------------------------------------------------------------------------------------

**Place the Share button in a convenient location, like a toolbar, to make it easy for people to start sharing or collaborating.** In iOS 16, the system-provided share sheet includes ways to choose a file-sharing method and set permissions for a new collaboration; iPadOS 16 and macOS 13 introduce similar appearance and functionality in the sharing popover. In your SwiftUI app, you can also enable sharing by presenting a share link that opens the system-provided share sheet when people choose it; for developer guidance, see [`ShareLink`](/documentation/SwiftUI/ShareLink)
.

**If necessary, customize the share sheet or sharing popover to offer the types of file sharing your app supports.** If you use CloudKit, you can add support for sending a copy of a file by passing both the file and your collaboration object to the share sheet. Because the share sheet has built-in support for multiple items, it automatically detects the file and makes the “send copy” functionality available. With iCloud Drive, your collaboration object supports “send copy” functionality by default. For custom collaboration, you can support “send copy” functionality in the share sheet by including a file — or a plain text representation of it — in your collaboration object.

**Write succinct phrases that summarize the sharing permissions you support.** For example, you might write phrases like “Everyone can make changes” or “Everyone can view.” The system uses your permission summary in a button that reveals a set of sharing options that people use to define the collaboration.

**Provide a set of simple sharing options that streamline collaboration setup.** You can customize the view that appears when people choose the permission summary button to provide choices that reflect your collaboration functionality. For example, you might offer options that let people specify who can access the content and whether they can edit it or just read it, and whether collaborators can add new participants. Keep the number of custom choices to a minimum and group them in ways that help people understand them at a glance.

**Prominently display the collaboration button as soon as collaboration starts.** The system-provided collaboration button reminds people that the content is shared and identifies who’s sharing it. Because the collaboration button typically appears after people interact with the share sheet or sharing popover, it works well to place it next to the Share button.

**Provide custom actions in the collaboration popover only if needed.** Choosing the collaboration button in your app reveals a popover that consists of three sections. The top section lists collaborators and provides communication buttons that can open Messages or FaceTime, the middle section contains your custom items, and the bottom section displays a button people use to manage the shared file. You don’t want to overwhelm people with too much information, so it’s crucial to offer only the most essential items that people need while they use your app to collaborate. For example, Notes summarizes the most recent updates and provides buttons that let people get more information about the updates or view more activities.

**If it makes sense in your app, customize the title of the modal view’s collaboration-management button.** People choose this button — titled “Manage Shared File” by default — to reveal the collaboration-management view where they can change settings and add or remove collaborators. If you use CloudKit sharing, the system provides a management view for you; otherwise, you create your own.

**Consider posting collaboration event notifications in Messages.** Choose the type of event that occurred — such as a change in the content or the collaboration membership, or the mention of a participant — and include a universal link people can use to open the relevant view in your app. For developer guidance, see [`SWHighlightEvent`](/documentation/sharedwithyou/swhighlightevent)
.

[Platform considerations](/design/human-interface-guidelines/collaboration-and-sharing#Platform-considerations)
---------------------------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, or macOS. Not available in tvOS.*

### [visionOS](/design/human-interface-guidelines/collaboration-and-sharing#visionOS)

By default, the system supports screen sharing for an app running in the Shared Space by streaming the current window to other collaborators. If one person transitions the app to a Full Space while sharing is in progress, the system pauses the stream for other people until the app returns to the Shared Space. For guidance, see [Immersive experiences](/design/human-interface-guidelines/immersive-experiences)
.

### [watchOS](/design/human-interface-guidelines/collaboration-and-sharing#watchOS)

In your SwiftUI app running in watchOS, use [`ShareLink`](/documentation/SwiftUI/ShareLink)
 to present the system-provided share sheet.

[Resources](/design/human-interface-guidelines/collaboration-and-sharing#Resources)
-----------------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/collaboration-and-sharing#Related)

[Activity views](/design/human-interface-guidelines/activity-views)


#### [Developer documentation](/design/human-interface-guidelines/collaboration-and-sharing#Developer-documentation)

[Shared with You](/documentation/sharedwithyou)


[`ShareLink`](/documentation/SwiftUI/ShareLink)


#### [Videos](/design/human-interface-guidelines/collaboration-and-sharing#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/124/74342B30-92E9-48F3-B0F2-6E42C8FD9391/6506_wide_250x141_1x.jpg) Design for Collaboration with Messages](https://developer.apple.com/videos/play/wwdc2022/10015) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/124/9785075B-13E9-4631-AD74-77B814019BF4/6589_wide_250x141_1x.jpg) Enhance collaboration experiences with Messages](https://developer.apple.com/videos/play/wwdc2022/10095) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/124/39FE3E81-AB11-4FEE-AE05-37951E2ADB12/6587_wide_250x141_1x.jpg) Integrate your custom collaboration app with Messages](https://developer.apple.com/videos/play/wwdc2022/10093) 
[Change log](/design/human-interface-guidelines/collaboration-and-sharing#Change-log)
-------------------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | New page. |

