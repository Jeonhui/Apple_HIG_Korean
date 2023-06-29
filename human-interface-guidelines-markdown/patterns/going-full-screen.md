Going full screen
=================

iPhone, iPad, and Mac offer full-screen modes that can provide a distraction-free environment, often hiding system and app controls until people take action to reveal them.![A sketch of two outward-pointing arrows arranged in a vertical line extending from the upper-left to the bottom-right, suggesting expansion. The image is overlaid with rectangular and circular grid lines and is tinted orange to subtly reflect the orange in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/b07f350730ba32976cba9f14829b2ce1/patterns-going-full-screen-intro@2x.png)

Note

visionOS doesn’t support a full-screen mode. When a visionOS app runs alongside other apps in the Shared Space, people can concentrate on the content in one window by increasing its size. If the app also offers a more immersive experience, people can transition the app to a Full Space, where they can engage more deeply with content or perform a task without distractions. For guidance, see [Immersive experiences](/design/human-interface-guidelines/immersive-experiences)
.

[Best practices](/design/human-interface-guidelines/going-full-screen#Best-practices)
-------------------------------------------------------------------------------------

**Support full-screen mode when it makes sense for your experience.** People appreciate full-screen mode when they want to play a game, play media, or perform an in-depth task, but not every app provides such experiences. For example, Calculator in macOS doesn’t need to support full-screen mode, because people generally use it to perform calculations and paste the results into other locations.

**Maintain access to essential app features so people can complete their task without exiting full-screen mode.** For example, a full-screen media experience needs to make playback controls persistently available or easy to reveal when people need them.

**If necessary, adjust your interface to take advantage of the expanded space in full-screen mode.** The area available for a full-screen experience is generally larger than the non-full-screen area. In some cases, such as in macOS and visionOS, a window can grow in both width and height when people choose to enter full-screen mode. To keep essential content prominent and to use the extra space well, you might want to subtly adjust the proportions of your interface. If this type of adjustment makes sense in your app, avoid jarring transitions and make sure your interface remains instantly recognizable.

**Let people choose when to exit full-screen mode.** People generally don’t expect to exit full-screen mode automatically when they switch to another app or finish an absorbing activity, like playing a movie or game.

**In general, let people reveal the Dock while an iPadOS or macOS app is in full-screen mode.** It’s important to preserve access to the Dock so people can quickly open apps and other Dock items. An exception is in a game where the edges of the screen are part of the experience.

[Platform considerations](/design/human-interface-guidelines/going-full-screen#Platform-considerations)
-------------------------------------------------------------------------------------------------------

*Not supported in tvOS, visionOS, or watchOS.*

### [iOS, iPadOS](/design/human-interface-guidelines/going-full-screen#iOS-iPadOS)

**Allow auto-hiding of the Home Screen indicator when it makes sense.** With auto-hiding, the indicator fades out if people haven’t touched the screen for a few seconds, reappearing when they touch it again. Support this behavior only for viewing experiences like playing videos or photo slideshows and during gameplay.

### [macOS](/design/human-interface-guidelines/going-full-screen#macOS)

**Use the system-provided full-screen experience.** Using the system’s full-screen support ensures that your full-screen window works well in all contexts. For developer guidance, see [`toggleFullScreen(_:)`](/documentation/appkit/nswindow/1419527-togglefullscreen)
.

**If you use custom full-screen support, rely on system-defined areas to keep your full-screen window content unobscured.** For example, some Mac models include a camera housing that occupies an area at the top-center of the screen. Using the system’s full-screen support automatically accommodates this area; if you use a custom full-screen experience, you need to account for system-defined areas as you position your content. macOS provides two ways to help you position content when using a custom full-screen experience:

* The [`safeAreaInsets`](/documentation/appkit/nsscreen/3882821-safeareainsets)
 property contains top, bottom, left, and right values that define the safe area of the screen. Use the top value to inset your content from the top of the screen so that it remains unobscured.
* The [`auxiliaryTopLeftArea`](/documentation/appkit/nsscreen/3882915-auxiliarytopleftarea)
 and [`auxiliaryTopRightArea`](/documentation/appkit/nsscreen/3882916-auxiliarytoprightarea)
 properties define the rectangles at the top of the screen that represent unobscured areas left and right of the camera housing and outside of the safe area.

**Keep the toolbar visible when it’s necessary for accomplishing tasks; hide it when the focus is on content.** You can set a full-screen window to show the toolbar all the time, or only when people move the pointer to the top of the screen. Calendar, for example, always displays the toolbar, providing quick access to essential navigation and schedule-management controls. On the other hand, Preview hides the toolbar so people can focus on reading or viewing content. Note that the menu bar typically hides in full-screen mode unless people reveal it.

**Always let people enter Mission Control.** Even when your app is the only thing in focus, people expect to invoke Mission Control to preview and navigate other open windows, full-screen apps, desktops, and spaces. Respect the keyboard shortcuts and gestures people use to enter Mission Control, regardless of the type of experience your app provides.

**After people switch away from your full-screen app, help them resume where they left off when they return.** For example, a game or a slideshow needs to pause automatically when people leave the app so they don’t miss anything.

**Configure auxiliary windows for use in full-screen mode.** Full-screen auxiliary windows need proper configuration to display above full-screen content. For developer guidance, see [`fullScreenAuxiliary`](/documentation/appkit/nswindow/collectionbehavior/1419617-fullscreenauxiliary)
.

**If people expect to access files while they’re in your app, provide convenient ways to do so in full-screen mode.** Don’t make people exit full-screen mode to open files, import images, save files, or perform similar interactions. For example, you might implement an app-specific image browser that lets people open images in your app regardless of the current mode.

[Resources](/design/human-interface-guidelines/going-full-screen#Resources)
---------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/going-full-screen#Related)

[Layout](/design/human-interface-guidelines/layout)


[Multitasking](/design/human-interface-guidelines/multitasking)


#### [Developer documentation](/design/human-interface-guidelines/going-full-screen#Developer-documentation)

[`NSScreen`](/documentation/appkit/nsscreen)


[`NSWindow.CollectionBehavior`](/documentation/appkit/nswindow/collectionbehavior)


