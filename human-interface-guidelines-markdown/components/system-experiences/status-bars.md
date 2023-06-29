Status bars
===========

A status bar appears along the upper edge of the screen and displays information about the device’s current state, like the time, cellular carrier, and battery level.![A stylized representation of an iPhone status bar with labels showing the time and cellular, Wi-Fi, and battery levels. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/f26343633aeaea4ae5297fae42787bf2/components-status-bar-intro@2x.png)

[Best practices](/design/human-interface-guidelines/status-bars#Best-practices)
-------------------------------------------------------------------------------

**Obscure content under the status bar.** By default, the background of the status bar is transparent, allowing content beneath to show through. This can make it difficult to see the information presented in the status bar. If controls are visible behind the status bar, people may attempt to interact with them and be unable to do so. Be sure to keep the status bar readable and don’t imply that content behind it is interactive. There are several common techniques for doing this:

* Use a navigation bar that automatically displays a status bar background.
* Display a custom image, like a gradient or solid color, behind the status bar.
* Place a blurred view behind the status bar. For developer guidance, see [`UIBlurEffect`](/documentation/uikit/uiblureffect)
.

**Consider temporarily hiding the status bar when displaying full-screen media.** A status bar can be distracting when people are trying to focus on media. Temporarily hide these elements to provide a more immersive experience. The Photos app, for example, hides the status bar and other interface elements when people browse full-screen photos.

![A screenshot of the Photos app on iPhone, showing a photo above a horizontally scrolling list of other photos. The status bar is visible at the top of the screen and the toolbar is visible at the bottom.](https://docs-assets.developer.apple.com/published/f8d3ee25c6dd0998533f9f7c92ec1b95/status-bar@2x.png)![A screenshot of the Photos app on iPhone, showing a photo between black areas at the top and bottom of the screen.](https://docs-assets.developer.apple.com/published/b50a50d298e594949b8a43db338992ce/hidden-status-bar@2x.png)**Avoid permanently hiding the status bar.** Without a status bar, people have to leave your app to check the time or see if they have a Wi-Fi connection. Let people redisplay a hidden status bar with a simple, discoverable gesture. For example, when browsing full-screen photos in the Photos app, a single tap shows the status bar again.

[Platform considerations](/design/human-interface-guidelines/status-bars#Platform-considerations)
-------------------------------------------------------------------------------------------------

*No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/status-bars#Resources)
---------------------------------------------------------------------

#### [Developer documentation](/design/human-interface-guidelines/status-bars#Developer-documentation)

[`UIStatusBarStyle`](/documentation/uikit/uistatusbarstyle)


[`preferredStatusBarStyle`](/documentation/uikit/uiviewcontroller/1621416-preferredstatusbarstyle)


