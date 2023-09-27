June 21, 2023

 Updated to include guidance for visionOS. Navigation bars
===============

A navigation bar appears at the top of a window or screen, helping people navigate through a hierarchy of content.![A stylized representation of a navigation bar containing a back button, title text, and a compose icon. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/ed989dc263b39c20919e22d2e5e4d104/components-navigation-bar-intro@2x.png)

A navigation bar provides a natural place to display a title that can help people orient themselves in your app or game, and it can also include controls that affect the content below it.

macOS doesn’t provide a navigation bar. To support navigation in a macOS app, you often use a [sidebar](/design/human-interface-guidelines/sidebars)
 or a navigation control like a Back button in a [toolbar](/design/human-interface-guidelines/toolbars)
. Also, you typically display the title of a macOS [window](/design/human-interface-guidelines/windows)
 in the title bar.

[Best practices](/design/human-interface-guidelines/navigation-bars#Best-practices)
-----------------------------------------------------------------------------------

**Use the title area to describe the current window if it provides useful context.** A title helps people confirm their location as they navigate your app. However, if titling a navigation bar seems redundant, you can leave the title area empty. For example, Notes doesn’t title the current note because the first line of content typically supplies sufficient context. Your app’s name doesn’t provide useful information about your content hierarchy or any window or screen in your app, so it doesn’t work well as a title.

**Write a concise title.** Aim for a word or short phrase that distills the purpose of the window or screen. Using no more than about 15 characters tends to work well in most cases because it leaves enough room for a Back button and optional controls.

**Consider temporarily hiding the navigation bar to provide a distraction-free experience.** For example, in iOS, iPadOS, and macOS, Photos hides the navigation bar and other interface elements when people view full-screen photos. If you implement this type of behavior, let people restore the navigation bar by using a familiar gesture, like tapping or swiping down. Although a visionOS window can hide its navigation bar, people generally expect different types of immersive experiences while wearing Apple Vision Pro; for guidance, see [Immersive experiences](/design/human-interface-guidelines/immersive-experiences)
.

**Use the standard back button.** People know that the standard back button lets them retrace their steps through a hierarchy of information. If you implement a custom back button, make sure it still looks like a back button, behaves as people expect, matches the rest of your interface, and is consistently implemented throughout your app or game. If you replace the system-provided back button chevron with a custom image, you may need to supply a mask for your custom image, too. For example, iOS uses this mask to animate the button title during transitions.

**Make sure buttons that use text labels have enough room.** If your navigation bar includes more than one text-labeled button, the text of those buttons may appear to run together, making the buttons indistinguishable. Add separation by inserting a fixed-space item between the buttons. For developer guidance, see [`UIBarButtonSystemItemFixedSpace`](/documentation/uikit/uibarbuttonsystemitem/uibarbuttonsystemitemfixedspace)
.

[Platform considerations](/design/human-interface-guidelines/navigation-bars#Platform-considerations)
-----------------------------------------------------------------------------------------------------

*No additional considerations for tvOS. Not supported in macOS.*

### [iOS, iPadOS](/design/human-interface-guidelines/navigation-bars#iOS-iPadOS)

**Consider using a segmented control in a navigation bar to flatten the information hierarchy.** For example, Phone uses a segmented control in the navigation bar of the Recents tab to let people switch between viewing all recent calls or only missed ones. If a design like this makes sense in your app, place a segmented control in the navigation bar only at the top level of the hierarchy, and be sure to create accurate back-button labels for the second-level screens. For guidance, see [Segmented controls](/design/human-interface-guidelines/segmented-controls)
.

**Use a large title to help people stay oriented as they navigate and scroll.** For example, Phone uses the large title to clarify the active tab, while Music uses large titles to differentiate content areas like albums, artists, playlists, and radio. By default, a large title transitions to a standard title as people begin scrolling the content, and transitions back to large when people scroll to the top, reminding them of their current location. For developer guidance, see [`prefersLargeTitles`](/documentation/uikit/uinavigationbar/2908999-preferslargetitles)
.

![A partial screenshot of the Contacts app on iPhone, highlighted to emphasize the navigation bar. The contacts list has been scrolled up so that the navigation bar uses the standard title.](https://docs-assets.developer.apple.com/published/64bf477af9262d7c9b12e0aebe8ef1f1/navigation-bar-standard@2x.png)Standard title![A partial screenshot of the Contacts app on iPhone, highlighted to emphasize the navigation bar. The contacts list has been scrolled down so that the navigation bar uses the large title.](https://docs-assets.developer.apple.com/published/0e3fa2350b27ffbbe840a57281bbaabf/navigation-bar-large@2x.png)Large title**Consider hiding the border of a large-title navigation bar to enhance the sense of connection between title and content.** Use caution applying this design to a standard-title navigation bar, though, because the bar’s title and buttons might be harder to distinguish without a visible border. In contrast, you might want to maintain consistency between the primary and secondary views in a Split View on iPad by using the borderless style in both. You can hide the bottom border of a navigation bar by removing the bar’s shadow (the border automatically reappears when people scroll the content area).

### [visionOS](/design/human-interface-guidelines/navigation-bars#visionOS)

To maintain the legibility of navigation bar items as content scrolls behind them, visionOS uses a variable blur in the bar background. The variable blur anchors the bar above the scrolling content while letting the view’s glass material remain uniform and undivided.

**Prefer using standard components in a navigation bar.** In visionOS, navigation bar corners use a 60-pt continuous curve. By default, standard buttons, text fields, headers, and footers have corner radii that maintain concentricity with bar corners. If you need to create a custom component, you can use the following formula to help ensure that its corner radius is also concentric with the bar’s corners:

`radius = 60 pt - padding`, where `radius` is a custom component’s corner radius and `padding` is the value of the top padding or the bottom padding, if these values are identical.

**Use a large title to help people stay oriented as they navigate and scroll.** It generally works well when you display a large title in the view that’s at the top of a navigation stack, while centering a standard title in the navigation bar of all other views in the stack. By default, a large title transitions to a standard title as people begin scrolling the content, and transitions back to large when people scroll to the top, reminding them of their current location. For developer guidance, see [`prefersLargeTitles`](/documentation/uikit/uinavigationbar/2908999-preferslargetitles)
.

### [watchOS](/design/human-interface-guidelines/navigation-bars#watchOS)

The navigation bar appears at the top edge of the Apple Watch screen. The system offers space for a title, the time, and two buttons.

If the navigation bar doesn’t include any buttons, the system displays the time on the top trailing edge, and a large title on the leading edge, just below the time. However, watchOS resizes and relocates the title and time to accommodate top toolbar buttons.

![A screenshot that shows the time on the upper right and a large title on the upper left of the screen on Apple Watch.](https://docs-assets.developer.apple.com/published/cd681c4e38eff49162db8102e5f2b48f/nav-bar-watch-no-buttons@2x.png)![A screenshot that shows a back button on the upper left and the title and time on the upper right of the screen on Apple Watch.](https://docs-assets.developer.apple.com/published/4f5bb22834b906569c7288f3fcb381c9/nav-bar-watch-leading-button@2x.png)![A screenshot that shows an Information button on the upper left, the title and time in the center at top, and an Add button on the upper right of the screen on Apple Watch.](https://docs-assets.developer.apple.com/published/2e97316e3a50d67d1af182889c3052c0/nav-bar-watch-two-buttons@2x.png)By default, watchOS displays a back button when displaying hierarchical information.

Important

The clock appears in the navigation bar of every nonmodal app screen. You can’t remove the clock, so be sure to account for it in your designs.

Inset your content so that it aligns it with the navigation bar buttons, title, and time. You can also use the safe area insets to avoid having your content clipped by the rounded corners. For guidance, see [Layout](/design/human-interface-guidelines/layout)
.

![An illustration representing a screen on Apple Watch. A blue rectangle shows the inset margins for the navigation bar's back button, time and title.](https://docs-assets.developer.apple.com/published/6c78638afee5434abafa2cba59e2485d/status-bar-guides@2x.png)

[Resources](/design/human-interface-guidelines/navigation-bars#Resources)
-------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/navigation-bars#Related)

[Tab bars](/design/human-interface-guidelines/tab-bars)


[Sidebars](/design/human-interface-guidelines/sidebars)


#### [Developer documentation](/design/human-interface-guidelines/navigation-bars#Developer-documentation)

[`NavigationView`](/documentation/SwiftUI/NavigationView)


[`UINavigationBar`](/documentation/uikit/uinavigationbar)


#### [Videos](/design/human-interface-guidelines/navigation-bars#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/124/95386734-286A-4C41-8073-28AC9A155F44/6490_wide_250x141_1x.jpg) Explore navigation design for iOS](https://developer.apple.com/videos/play/wwdc2022/10001) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/124/6E076CE0-7DDF-4471-B6F0-005ADF9C7960/6500_wide_250x141_1x.jpg) What’s new in iPad app design](https://developer.apple.com/videos/play/wwdc2022/10009) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/7/2546ECBD-6443-41EC-921D-6429026F8B67/1700_wide_250x141_1x.jpg) Essential Design Principles](https://developer.apple.com/videos/play/wwdc2017/802) 
[Change log](/design/human-interface-guidelines/navigation-bars#Change-log)
---------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance for using navigation bars in watchOS. |

