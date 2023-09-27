iMessage apps and stickers
==========================

An iMessage app can help people share content, collaborate, and even play games with others in a conversation; stickers are images that people can use to decorate a conversation.![A sketch of the iMessage App Store icon. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/8a7764e72eeafa784a8f5343e1242096/technologies-iMessage-Apps-intro@2x.png)

An iMessage app or sticker pack is available within the context of a Messages conversation and also in effects in both Messages and FaceTime. You can create an iMessage app or sticker pack as a standalone app or as an app extension within your iOS or iPadOS app. For developer guidance, see [Messages](/documentation/messages)
 and [Adding Sticker Packs and iMessage Apps to Effects in Messages and FaceTime](/documentation/messages/adding_sticker_packs_and_imessage_apps_to_effects_in_messages_and_facetime)
.

[Best practices](/design/human-interface-guidelines/imessage-apps-and-stickers#Best-practices)
----------------------------------------------------------------------------------------------

**Prefer providing one primary experience in your iMessage app.** People are in a conversational flow when they choose your app, so your functionality or content needs to be easy to understand and immediately available. If you want to provide multiple types of functionality or different collections of content, consider creating a separate iMessage app for each one.

**Consider surfacing content from your iOS or iPadOS app.** For example, your iMessage app could offer app-specific information that people might want to share — such as a shopping list or a trip itinerary — or support a focused, collaborative task, like deciding where to go for a meal or which movie to watch.

**Present essential features in the compact view.** People can experience your iMessage app in a compact view that appears below the message transcript, or they can expand the view to occupy most of the window. Make sure the most frequently used items are available in the compact view, reserving additional content and features for the expanded view.

**In general, let people edit text only in the expanded view.** The compact view occupies roughly the same space as the keyboard. To ensure that the iMessage app’s content remains visible while people edit, display the keyboard in the expanded view.

**Create stickers that are expressive, inclusive, and versatile.** Whether your stickers are rich, static images or short animations, make sure that each one remains legible against a wide range of backgrounds and when rotated or scaled. You can also use transparency to help people visually integrate a sticker with text, photos, and other stickers.

**For each sticker, provide a localized alternative description.** VoiceOver can help people use your sticker pack by speaking a sticker’s alternative description.

[Specifications](/design/human-interface-guidelines/imessage-apps-and-stickers#Specifications)
----------------------------------------------------------------------------------------------

### [Icon sizes](/design/human-interface-guidelines/imessage-apps-and-stickers#Icon-sizes)

The icon for an iMessage app or sticker pack can appear in Messages, the App Store, notifications, and Settings. After people install your iMessage app or sticker pack, its icon also appears in the app drawer in the Messages app.

You supply a square-cornered icon for each extension you offer, and the system automatically applies a mask that rounds the corners.

To ensure that your icon looks great in any context and on various devices, create a square-cornered icon in the following sizes:



| Usage | @2x (pixels) | @3x (pixels) |
| --- | --- | --- |
| Messages, notifications | 148x110 | - |
|  | 143x100 | - |
|  | 120x90 | 180x135 |
|  | 64x48 | 96x72 |
|  | 54x40 | 81x60 |
| Settings | 58x58 | 87x87 |
| App Store | 1024x1024 | 1024x1024 |

### [Sticker sizes](/design/human-interface-guidelines/imessage-apps-and-stickers#Sticker-sizes)

Messages supports small, regular, and large stickers. Pick the size that works best for your content and prepare all of your stickers at that size; don’t mix sizes within a single sticker pack. Messages displays stickers in a grid, organized differently for different sizes.

![An illustration showing a grid of small stickers in the bottom half of an iPhone screen. Twelve stickers are visible in the area, arranged in three rows of four.](https://docs-assets.developer.apple.com/published/0f6da0a29a3a2a10affb0f959413a726/sticker-sizes-small@2x.png)Small![An illustration showing a grid of regular stickers in the bottom half of an iPhone screen. Six stickers are fully visible in the area, followed by a partial row of three additional stickers.](https://docs-assets.developer.apple.com/published/d75c65ed3464f44d874fbf7fecd8c79b/sticker-sizes-regular@2x.png)Regular![An illustration showing a grid of large stickers in the bottom half of an iPhone screen. Two stickers are fully visible in the area, followed by a partial row of two additional stickers.](https://docs-assets.developer.apple.com/published/78613165683c644d5daba8ee9167f9b5/sticker-sizes-large@2x.png)LargeCreate your sticker images using the following @3x dimensions for the sticker size you chose. If necessary, the system generates @2x and @1x versions by downscaling the images at runtime. For developer guidance, see [`MSStickerSize`](/documentation/messages/msstickersize)
.



| Sticker size | @3x dimensions (pixels) |
| --- | --- |
| Small | 300x300 |
| Regular | 408x408 |
| Large | 618x618 |

A sticker file must be 500 KB or smaller in size. For each supported format, the table below provides guidance for using transparency and animation.



| Format | Transparency | Animation |
| --- | --- | --- |
| PNG | 8-bit | No |
| APNG | 8-bit | Yes |
| GIF | Single-color | Yes |
| JPEG | No | No |

[Platform considerations](/design/human-interface-guidelines/imessage-apps-and-stickers#Platform-considerations)
----------------------------------------------------------------------------------------------------------------

*No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/imessage-apps-and-stickers#Resources)
------------------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/imessage-apps-and-stickers#Related)

[iMessage Apps and Stickers](https://developer.apple.com/imessage/)


#### [Developer documentation](/design/human-interface-guidelines/imessage-apps-and-stickers#Developer-documentation)

[Messages](/documentation/messages)


[Adding Sticker Packs and iMessage Apps to Effects in Messages and FaceTime](/documentation/messages/adding_sticker_packs_and_imessage_apps_to_effects_in_messages_and_facetime)


#### [Videos](/design/human-interface-guidelines/imessage-apps-and-stickers#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/7/FC4A4C67-CCE9-46D5-9376-D071D53B4FB2/1925_wide_250x141_1x.jpg) Express Yourself!](https://developer.apple.com/videos/play/wwdc2017/820) 
[Change log](/design/human-interface-guidelines/imessage-apps-and-stickers#Change-log)
--------------------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| May 2, 2023 | Consolidated guidance into one page. |

