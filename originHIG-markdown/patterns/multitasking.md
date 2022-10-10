# **[patterns] multitasking**

# Multitasking lets people switch quickly from one app to another, performing tasks in each.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-multitasking-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-multitasking-intro-dark_2x.png)

People expect to use multitasking on their devices, and they may think something is wrong if your app doesn’t allow it. With rare exceptions — such as some full-screen–only iPad apps — every app needs to work well with multitasking.

In addition to app switching, multitasking can enable different experiences on different devices.

On iPhone, multitasking lets people use FaceTime or watch a video in Picture in Picture while they also use a different app.

![https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/app-switcher-iphone_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/app-switcher-iphone_2x.png)

The app switcher displays all currently open apps.

![https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/pip-iphone_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/pip-iphone_2x.png)

A current FaceTime call can continue while people use another app.

On iPad, people can view and interact with the windows of several different apps at the same time. An individual app can also enable multiple windows, which lets people view and interact with more than one window in the same app at one time.

• [Multitasking](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking#)
• [Multiple windows](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking#)

-

![https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/multitasking-ipad-three-windows_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/multitasking-ipad-three-windows_2x.png)

With multitasking, windows from several apps — like Notes, Maps, and Photos — can be available onscreen at the same time.


Apple TV, people can play or browse content while also playing movies or TV shows in Picture in Picture (where supported).

On a Mac, multitasking is the default user experience because people typically run more than one app at a time, switching between windows and tasks as they work.

In contrast, watchOS makes it easy for people to switch between favorite or recently used apps, but people don’t open more than one app at a time on their watch.

# **Best practices**

A great multitasking experience helps people accomplish tasks in multiple apps by instantly pausing the current context when they switch away and seamlessly restoring it when they switch back. Because you don’t know when people will initiate multitasking, your app or game always needs to be prepared to save and restore their context.

**Pause activities that require people’s attention or active participation when they switch away.** If your app is a game or a media-viewing app, for example, make sure people don’t miss anything when they switch to another app. When they switch back, let them continue as if they never left.

**Respond smoothly to audio interruptions.** Occasionally, audio from another app or the system itself may interrupt your app’s audio. For example, an incoming phone call or a music playlist initiated by Siri might interrupt your app’s audio. When situations like these occur, people expect your app to respond in the following ways:

- Pause audio indefinitely for primary audio interruptions, such as playing music, podcasts, or audiobooks.
- Temporarily lower the volume or pause the audio for shorter interruptions, such as GPS directional notifications, and resume the original volume or playback when the interruption ends.

For guidance, see [Playing audio](https://developer.apple.com/design/human-interface-guidelines/patterns/playing-audio).

**Finish user-initiated tasks in the background.** When someone starts a task, they expect it to finish even if they switch away from your app. If your app is in the middle of performing a task that doesn’t need additional input, complete it in the background before suspending.

**Use notifications sparingly.** Your app can send notifications when it’s suspended or running in the background. If people start an important or time-sensitive task in your app, and then switch away from it, they might appreciate receiving a notification when the task completes so they can switch back to your app and take the next step. In contrast, people don’t generally need to know the moment a routine or secondary task completes. In this scenario, avoid sending an unnecessary notification; instead, let people check on the task when they return to your app. For guidance, see [Managing notifications](https://developer.apple.com/design/human-interface-guidelines/patterns/managing-notifications).

# **Platform considerations**

*No additional considerations for iOS, macOS, or tvOS. Not supported in watchOS.*

# **iPadOS**

### **Multitasking on iPad**

iPadOS can present multitasking windows in a variety of configurations, supporting various workflows. The system also provides multitasking controls — which let people switch multitasking configurations — and the app shelf, which lets people access all open windows in an app.

![https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/multitasking-controls_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/multitasking-controls_2x.png)

Multitasking controls

![https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/app-shelf_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/app-shelf_2x.png)

App shelf

People can choose one of the following configurations to open multitasking windows on iPad.

- *Slide Over* opens a second window in an overlay while the first window continues in full screen. People can change the onscreen location of the Slide Over window, or hide it offscreen and retrieve it later. People can also open multiple windows in Slide Over, where they form a stack.
- *Split View* displays two windows side by side, letting people resize the relative areas of the windows and interact with both. While viewing side-by-side windows in Split View, people can also open a third window in Slide Over.
- *Picture in Picture* opens a video in a movable, resizable window that floats above the full-screen app.

• [Slide Over](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking#)
• [Split View](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking#)
• [Picture in Picture](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking#)

-

![https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/slideover_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/slideover_2x.png)


**NOTE**Apps don’t control multitasking configurations or receive any indication of the ones that people choose.

To help your iPad app respond correctly when people open it in Split View or Slide Over, make sure it [adapts gracefully to different screen sizes](https://developer.apple.com/design/human-interface-guidelines/foundations/layout); for developer guidance, see [Multitasking on iPad](https://developer.apple.com/documentation/uikit/app_and_environment/multitasking_on_ipad). To learn more about how people use iPad multitasking features, see [Use multitasking on your iPad](https://support.apple.com/en-us/HT207582).

### **Multiple windows on iPad**

Conceptually, iPad apps tend to use two types of windows to provide content:

- A *primary* window presents the app’s full hierarchy, providing access to all of the app’s objects and the actions associated with them. For example, Mail uses a primary window to present all mailboxes and message lists.
- An *auxiliary* window presents a specific task or area in the app, often using a modal presentation. Dedicated to one experience, an auxiliary window doesn’t enable navigation to other app areas, and it typically includes buttons people use to close it after completing the task. For example, Mail uses an auxiliary window to present a single message.

In iPadOS 15 and later, you can specify a presentation style that determines the initial appearance of each window that people open in your app. Although people can reposition a window after opening it, specifying a presentation style can visually reinforce the nature of a window’s task or content. iPadOS defines the following presentation styles:

- Prominent. A modal presentation that elevates the window, dimming the surrounding areas and preventing interaction with them.
- Standard. A side-by-side presentation that enables interaction with peer windows, each of which supports the app’s full functionality.
- Automatic. A presentation that the system chooses based on the context in which your app requests the window.

**TIP**If you simply need to let people view a file, you can present it without creating your own window, but you must support multiple windows in your app. For developer guidance, see [QLPreviewSceneActivationConfiguration](https://developer.apple.com/documentation/quicklook/qlpreviewsceneactivationconfiguration/).

**Use the prominent style to present a self-contained task people can complete without opening other parts of your app.** For example, the prominent style works well to enable document editing or another task that’s scoped to a specific file or collection of content. Be sure a prominent window is also useful on its own; avoid using it to present secondary tasks, supplemental actions, or choosing items that affect the main task.

**Use the standard style to present multiple versions of the same task or content.** For example, Safari uses the standard style to help people view and interact with two browsing windows onscreen at the same time.

**Open a new window only when people take an explicit action.** For example, people can tap the Add (+) button in the app shelf or App Exposé, or choose a menu item. Avoid surprising people by opening a new window they don’t request.

**Make sure your app’s primary windows support every task that you enable.** Multiple windows can offer convenient and efficient workflows, but people always need to be able to access every app feature in each primary window.

**Preserve the state in each window that people open.** When people return to a window, they expect it to be in the same state in which they left it. For developer guidance, see [Restoring your app’s state](https://developer.apple.com/documentation/uikit/uiscenedelegate/restoring_your_app_s_state).

**Consider letting people use a gesture to open content in a new window.** For example, people can use the pinch gesture to expand a Notes item into a new window. A gesture-enabled transition always uses the prominent presentation style, making the resulting modal window feel like a natural consequence of expanding the item or task. For developer guidance, see [collectionView(_:sceneActivationConfigurationForItemAt:point:)](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/3752185-collectionview) (to transition from a collection view item) or [UIWindowScene.ActivationInteraction](https://developer.apple.com/documentation/uikit/uiwindowscene/activationinteraction) (to transition from an item in any other view).

**Consider providing a menu item that lets people open content in a new window.** When you enable this behavior, the menu presents an “Open in new window” item when your app runs on iPad or on a Mac using Mac Catalyst, but not when your app runs on iPhone. If it makes sense in your app, you can supply an alternative item to display when the app runs on iPhone, such as “Show details...”. You can add an “Open in new window” item to a context menu or to menus attached to buttons and bar button items. For developer guidance, see [UIWindowScene.ActivationAction](https://developer.apple.com/documentation/uikit/uiwindowscene/activationaction/).

**Avoid specifying a layout when providing a way to open content in a new window.** Because you don’t know which multitasking configuration people are using, avoid offering menu items like “Open in split view” or “Open in front.”

**Use the term *window* in user-facing content.** The system refers to app windows as *windows* regardless of type. Using different terms — including *scene*, which refers to window implementation — is likely to confuse people.