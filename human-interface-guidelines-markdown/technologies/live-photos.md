Live Photos
===========

Live Photos lets people capture favorite memories in a sound- and motion-rich interactive experience that adds vitality to traditional still photos.![A sketch of the Live Photos icon. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/dc6a4a0eb43d1336511cf15379c03a04/technologies-Live-Photos-intro@2x.png)

When Live Photos is available, the Camera app captures additional content — including audio and extra frames — before and after people take a photo. People press a Live Photo to see it spring to life.

 [Play](#) 
[Best practices](/design/human-interface-guidelines/live-photos#Best-practices)
-------------------------------------------------------------------------------

**Apply adjustments to all frames.** If your app lets people apply effects or adjustments to a Live Photo, make sure those changes are applied to the entire photo. If you don’t support this, give people the option of converting it to a still photo.

**Keep Live Photo content intact.** It’s important for people to experience Live Photos in a consistent way that uses the same visual treatment and interaction model across all apps. Don’t disassemble a Live Photo and present its frames or audio separately.

**Implement a great photo sharing experience.** If your app supports photo sharing, let people preview the entire contents of Live Photos before deciding to share. Always offer the option to share Live Photos as traditional photos.

**Clearly indicate when a Live Photo is downloading and when the photo is playable.** Show a progress indicator during the download process and provide some indication when the download is complete.

**Display Live Photos as traditional photos in environments that don’t support Live Photos.** Don’t attempt to replicate the Live Photos experience provided in a supported environment. Instead, show a traditional, still representation of the photo.

**Make Live Photos easily distinguishable from still photos.** The best way to identify a Live Photo is through a hint of movement. Note that there are no built-in Live Photo motion effects, like the one that occurs as you swipe through photos in the full-screen browser of Photos app. Any motion effects like this must be custom designed and implemented. In cases where movement isn’t possible, show a system-provided badge above the photo. This badge can be displayed as an overlay with a shadow or as a solid color without a shadow. A badge variant is also available for situations where a Live Photo appears as a traditional photo. Never include a playback button that could be interpreted as a video playback button.

![A screenshot of a Live Photo displayed on a sharing view in the Photos app on iPhone. A system-provided badge appears in the top-left corner of the Live Photo.](https://docs-assets.developer.apple.com/published/82f0fb634209b1a6243bb41e22669501/live-badge-a@2x.png)![A screenshot of a Live Photo in the compose area of a new message view in the Messages app on iPhone. A system-provided badge appears in the top-left corner of the Live Photo.](https://docs-assets.developer.apple.com/published/70563467e835a0064679a2fc07896499/live-badge-b@2x.png)**Keep badge placement consistent.** If you show a badge, put it in the same location on every photo. Typically, a badge looks best in a corner of a photo.

[Platform considerations](/design/human-interface-guidelines/live-photos#Platform-considerations)
-------------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, or tvOS. Not supported in watchOS.*

### [visionOS](/design/human-interface-guidelines/live-photos#visionOS)

In visionOS, people can view a Live Photo, but they can’t capture one.

[Resources](/design/human-interface-guidelines/live-photos#Resources)
---------------------------------------------------------------------

#### [Videos](/design/human-interface-guidelines/live-photos#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/119/80B5C413-F0CF-44C1-9EE1-7BBC8C8978F0/4937_wide_250x141_1x.jpg) What’s new in camera capture](https://developer.apple.com/videos/play/wwdc2021/10047) 
