June 21, 2023

 Updated to include guidance for visionOS. Multitasking
============

Multitasking lets people switch quickly from one app to another, performing tasks in each.![A sketch of two side-by-side windows in a split view arrangement, suggesting multitasking. The image is overlaid with rectangular and circular grid lines and is tinted orange to subtly reflect the orange in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/94f1391bf700ee7af09ad0f966dd7b36/patterns-multitasking-intro@2x.png)

People expect to use multitasking on their devices, and they may think something is wrong if your app doesn’t allow it. With rare exceptions — such as some full-screen–only iPad apps and Apple Vision Pro apps running in a Full Space — every app needs to work well with multitasking.

In addition to app switching, multitasking can present different experiences on different devices.

On Vision Pro, people can run multiple apps at the same time in the Shared Space, viewing and switching between windows and volumes throughout their space.

On iPhone, multitasking lets people use FaceTime or watch a video in Picture in Picture while they also use a different app.

![A screenshot of the app switcher on iPhone, showing 4 open apps.](https://docs-assets.developer.apple.com/published/76c35a81ee48050caa1092092a3fc2cb/app-switcher-iphone@2x.png)The app switcher displays all currently open apps.![A screenshot of Calendar on iPhone. On top of the month view, a small image in the top-right corner shows the person currently in a FaceTime call.](https://docs-assets.developer.apple.com/published/09dd5e7896ed85b49efae97a3e41cf0b/pip-iphone@2x.png)A current FaceTime call can continue while people use another app.On iPad, people can view and interact with the windows of several different apps at the same time. An individual app can also support multiple open windows, which lets people view and interact with more than one window in the same app at one time.

* [Multitasking](#)
* [Multiple windows](#)
![A screenshot of 3 open apps on iPad in landscape. In the foreground, Weather is in a narrow window on the left. Behind Weather are Maps and Photos, both of which occupy one half the width of the screen.](https://docs-assets.developer.apple.com/published/7dc0756b5bba12813bfa15ae034c2034/multitasking-ipad-three-windows@2x.png)With multitasking, windows from several apps — like Weather, Maps, and Photos — can be available onscreen at the same time.![A screenshot of the app switcher on iPad in landscape, showing two open windows from the same app.](https://docs-assets.developer.apple.com/published/5e96a7b72a92cdb46aa479770d918d78/multiwindow@2x.png)Calendar lets people open multiple calendar windows at the same time.On Apple TV, people can play or browse content while also playing movies or TV shows in Picture in Picture (where supported).

On a Mac, multitasking is the default user experience because people typically run more than one app at a time, switching between windows and tasks as they work. When multiple app windows are open, macOS applies drop shadows that make the windows appear layered on the desktop, and applies other visual effects to help people distinguish different window states; for guidance, see [macOS window states](/design/human-interface-guidelines/windows#macOS-window-states)
.

In contrast, watchOS makes it easy for people to switch between favorite or recently used apps, but people don’t open more than one app at a time on their watch.

[Best practices](/design/human-interface-guidelines/multitasking#Best-practices)
--------------------------------------------------------------------------------

A great multitasking experience helps people accomplish tasks in multiple apps by instantly pausing the current context when they switch away and seamlessly restoring it when they switch back. Because you don’t know when people will initiate multitasking, your app or game always needs to be prepared to save and restore their context.

**In iOS and iPadOS, pause activities that require people’s attention or active participation when they switch away.** If your app is a game or a media-viewing app, for example, make sure people don’t miss anything when they switch to another app. When they switch back, let them continue as if they never left.

**Respond smoothly to audio interruptions.** Occasionally, audio from another app or the system itself may interrupt your app’s audio. For example, an incoming phone call or a music playlist initiated by Siri might interrupt your app’s audio. When situations like these occur, people expect your app to respond in the following ways:

* Pause audio indefinitely for primary audio interruptions, such as playing music, podcasts, or audiobooks.
* Temporarily lower the volume or pause the audio for shorter interruptions, such as GPS directional notifications, and resume the original volume or playback when the interruption ends.

For guidance, see [Playing audio](/design/human-interface-guidelines/playing-audio)
.

**Finish user-initiated tasks in the background.** When someone starts a task, they expect it to finish even if they switch away from your app. If your app is in the middle of performing a task that doesn’t need additional input, complete it in the background before suspending.

**Use notifications sparingly.** Your app can send notifications when it’s suspended or running in the background. If people start an important or time-sensitive task in your app, and then switch away from it, they might appreciate receiving a notification when the task completes so they can switch back to your app and take the next step. In contrast, people don’t generally need to know the moment a routine or secondary task completes. In this scenario, avoid sending an unnecessary notification; instead, let people check on the task when they return to your app. For guidance, see [Managing notifications](/design/human-interface-guidelines/managing-notifications)
.

[Platform considerations](/design/human-interface-guidelines/multitasking#Platform-considerations)
--------------------------------------------------------------------------------------------------

*No additional considerations for iOS, macOS, or tvOS. Not supported in watchOS.*

### [iPadOS](/design/human-interface-guidelines/multitasking#iPadOS)

#### [Multitasking on iPad](/design/human-interface-guidelines/multitasking#Multitasking-on-iPad)

iPadOS can present multitasking windows in a variety of configurations, supporting various workflows. The system also provides multitasking controls — which let people switch multitasking configurations — and the app shelf, which lets people access all open windows in an app.

![An illustration of the multitasking controls in iPadOS.](https://docs-assets.developer.apple.com/published/a26b482a66febddbf7b4cf2a11ebcbae/multitasking-controls@2x.png)Multitasking controls![An illustration of the app shelf on iPad, containing two open windows in an app and a control that lets people open a new window.](https://docs-assets.developer.apple.com/published/dcd70aae616b95cd9297363fa5bbb117/app-shelf@2x.png)App shelfPeople can choose one of the following configurations to open multitasking windows on iPad.

* *Slide Over* opens a second window in an overlay while the first window continues in full screen. People can change the onscreen location of the Slide Over window, or hide it offscreen and retrieve it later. People can also open multiple windows in Slide Over, where they form a stack.
* *Split View* displays two windows side by side, letting people resize the relative areas of the windows and interact with both. While viewing side-by-side windows in Split View, people can also open a third window in Slide Over.
* *Picture in Picture* opens a video in a movable, resizable window that floats above the full-screen app.

* [Slide Over](#)
* [Split View](#)
* [Picture in Picture](#)
![An illustration that represents the Mail app on iPad in landscape with the Notes app in a Slide Over window near the right edge.](https://docs-assets.developer.apple.com/published/5aa076a0f767cc3bc64f873a2d64635c/slideover@2x.png)

![An illustration that represents the Notes and Photos apps on iPad in landscape, in which each app takes one half of the screen.](https://docs-assets.developer.apple.com/published/3593a402f5bb9b8ccca4c4e40ad0461a/split-view@2x.png)

![An illustration that represents Mail on iPad in landscape with a small picture-in-picture window in the bottom-right corner that represents a video player.](https://docs-assets.developer.apple.com/published/ed4f8181bb459d4ae6b6bf21150f9698/pip-ipad@2x.png)

Note

Apps don’t control multitasking configurations or receive any indication of the ones that people choose.

To help your iPad app respond correctly when people open it in Split View or Slide Over, make sure it adapts gracefully to different screen sizes. For guidance, see [Layout](/design/human-interface-guidelines/layout)
; for developer guidance, see [Multitasking on iPad](/documentation/uikit/app_and_environment/multitasking_on_ipad)
. To learn more about how people use iPad multitasking features, see [Use multitasking on your iPad](https://support.apple.com/en-us/HT207582)
.

#### [Multiple windows on iPad](/design/human-interface-guidelines/multitasking#Multiple-windows-on-iPad)

Conceptually, iPad apps tend to use two types of windows to provide content:

* A *primary* window presents the app’s full hierarchy, providing access to all of the app’s objects and the actions associated with them. For example, Mail uses a primary window to present all mailboxes and message lists.
* An *auxiliary* window presents a specific task or area in the app, often using a modal presentation. Dedicated to one experience, an auxiliary window doesn’t allow navigation to other app areas, and it typically includes buttons people use to close it after completing the task. For example, Mail uses an auxiliary window to present a single message.

In iPadOS 15 and later, you can specify a presentation style that determines the initial appearance of each window that people open in your app. Although people can reposition a window after opening it, specifying a presentation style can visually reinforce the nature of a window’s task or content. iPadOS defines the following presentation styles:

* Prominent. A modal presentation that elevates the window, dimming the surrounding areas and preventing interaction with them.
* Standard. A side-by-side presentation that allows interaction with peer windows, each of which supports the app’s full functionality.
* Automatic. A presentation that the system chooses based on the context in which your app requests the window.

Tip

If you simply need to let people view a file, you can present it without creating your own window, but you must support multiple windows in your app. For developer guidance, see [`QLPreviewSceneActivationConfiguration`](/documentation/quicklook/qlpreviewsceneactivationconfiguration)
.

**Use the prominent style to present a self-contained task people can complete without opening other parts of your app.** For example, the prominent style works well for document editing or another task that’s scoped to a specific file or collection of content. Be sure a prominent window is also useful on its own; avoid using it to present secondary tasks, supplemental actions, or choosing items that affect the main task.

**Use the standard style to present multiple versions of the same task or content.** For example, Safari uses the standard style to help people view and interact with two browsing windows onscreen at the same time.

**Open a new window only when people take an explicit action.** For example, people can tap the Add (+) button in the app shelf or App Exposé, or choose a menu item. Avoid surprising people by opening a new window they don’t request.

**Make sure your app’s primary windows support every task in your app.** Multiple windows can offer convenient and efficient workflows, but people always need to be able to access every app feature in each primary window.

**Preserve the state in each window that people open.** When people return to a window, they expect it to be in the same state in which they left it. For developer guidance, see [Restoring Your App’s State](/documentation/uikit/uiscenedelegate/restoring_your_app_s_state)
.

**Consider letting people use a gesture to open content in a new window.** For example, people can use the pinch gesture to expand a Notes item into a new window. A gesture-based transition always uses the prominent presentation style, making the resulting modal window feel like a natural consequence of expanding the item or task. For developer guidance, see [`collectionView(_:sceneActivationConfigurationForItemAt:point:)`](/documentation/uikit/uicollectionviewdelegate/3752185-collectionview)
 (to transition from a collection view item) or [`UIWindowScene.ActivationInteraction`](/documentation/uikit/uiwindowscene/activationinteraction)
 (to transition from an item in any other view).

**Consider providing a menu item that lets people open content in a new window.** When you support this behavior, the menu presents an “Open in new window” item when your app runs on iPad or on a Mac using Mac Catalyst, but not when your app runs on iPhone. If it makes sense in your app, you can supply an alternative item to display when the app runs on iPhone, such as “Show details…”. You can add an “Open in new window” item to a context menu or to menus attached to buttons and bar button items. For developer guidance, see [`UIWindowScene.ActivationAction`](/documentation/uikit/uiwindowscene/activationaction)
.

**Avoid specifying a layout when providing a way to open content in a new window.** Because you don’t know which multitasking configuration people are using, avoid offering menu items like “Open in split view” or “Open in front.”

**Use the term *window* in user-facing content.** The system refers to app windows as *windows* regardless of type. Using different terms — including *scene*, which refers to window implementation — is likely to confuse people.

### [visionOS](/design/human-interface-guidelines/multitasking#visionOS)

In visionOS, only one window is active at a time in the Shared Space. When people switch focus from one window to another, the focused window becomes active and the unfocused window becomes more translucent and appears to recede along the z-axis. Closing an app window in the Shared Space transitions the app to the background without quitting it.

Note

When an app is the Now Playing app, closing its window automatically pauses audio playback; if people want to resume playback, they can do so in Control Center without opening the window.

**Avoid interfering with the system-provided multitasking behavior.** When people switch focus from one window to another, visionOS applies a feathered mask to the unfocused window to clarify its changed state. To avoid interfering with this visual feedback, don’t change the appearance of a window’s edges.

 [Play](#) 
**Don’t pause a window’s video playback when people move focus away from it.** In visionOS, as in macOS, people expect the playback they start in one window to continue while they view or perform a task in another window.

**Be prepared for situations where your audio can duck.** Unless an app is currently the Now Playing app, its audio can duck when people look away from it to another app.

[Resources](/design/human-interface-guidelines/multitasking#Resources)
----------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/multitasking#Related)

[Layout](/design/human-interface-guidelines/layout)


#### [Developer documentation](/design/human-interface-guidelines/multitasking#Developer-documentation)

[Responding to the launch of your app](/documentation/uikit/app_and_environment/responding_to_the_launch_of_your_app)


[Multitasking on iPad](/documentation/uikit/app_and_environment/multitasking_on_ipad)


#### [Videos](/design/human-interface-guidelines/multitasking#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/124/6E076CE0-7DDF-4471-B6F0-005ADF9C7960/6500_wide_250x141_1x.jpg) What’s new in iPad app design](https://developer.apple.com/videos/play/wwdc2022/10009) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/49/5C8F0205-3AE9-4647-870B-5C10FB7EA6FF/3520_wide_250x141_1x.jpg) Designed for iPad](https://developer.apple.com/videos/play/wwdc2020/10206) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/48/0FA460EB-3A3A-4DAC-B405-0D6C5D4F0D01/2704_wide_250x141_1x.jpg) Introducing Multiple Windows on iPad](https://developer.apple.com/videos/play/wwdc2019/212) 
[Change log](/design/human-interface-guidelines/multitasking#Change-log)
------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |

