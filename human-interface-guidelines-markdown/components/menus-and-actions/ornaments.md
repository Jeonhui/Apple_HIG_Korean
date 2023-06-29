June 21, 2023

 New page. Ornaments
=========

In visionOS, an ornament presents controls and information related to a window, without crowding or obscuring the window’s contents.![A stylized representation of an ornament at the bottom of a window shown on top of a grid that suggests the canvas of a design tool. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/a9012c3e7b1c5d47a4788aefd7a5b48c/components-ornaments-intro@2x.png)

An ornament floats in a plane that’s parallel to its associated window and slightly in front of it along the z-axis. If the associated window moves, the ornament moves with it, maintaining its relative position; if the window’s contents scroll, the controls or information in the ornament remain unchanged.

Ornaments can appear on any edge of a window and can contain UI components like buttons, segmented controls, and other views. The system uses ornaments to create and manage components like [toolbars](/design/human-interface-guidelines/toolbars)
, [tab bars](/design/human-interface-guidelines/tab-bars)
, and video playback controls; you can use an ornament to create a custom component.

[Best practices](/design/human-interface-guidelines/ornaments#Best-practices)
-----------------------------------------------------------------------------

**Consider using an ornament to present frequently needed controls or information in a consistent location that doesn’t clutter the window.** Because an ornament stays close to its window, people always know where to find it. For example, Music uses an ornament to offer Now Playing controls, ensuring that these controls remain in a predictable location that’s easy to find.

**Prefer an ornament — not a separate window — for offering supplementary controls and information.** Using an ornament to offer relevant functionality lets you avoid opening an additional window people have to manage separately.

**In general, keep an ornament visible.** It can make sense to hide an ornament when people dive into a window’s content — for example, when they watch a video or view a photo — but in most cases, people appreciate having consistent access to an ornament’s controls.

**Aim to keep an ornament’s width the same or narrower than the width of the associated window.** If an ornament is wider than its window, it can interfere with a tab bar or other vertical content on the window’s side.

**Consider using borderless buttons in an ornament.** By default, an ornament’s background is [glass](/design/human-interface-guidelines/materials#visionOS)
, so if you place a button directly on the background, it may not need a visible border. When people look at a borderless button in an ornament, the system automatically applies the hover affect to it (for guidance, see [Eyes](/design/human-interface-guidelines/eyes)
).

**Use system-provided toolbars and tab bars unless you need to create custom components.** In visionOS, toolbars and tab bars automatically appear as ornaments, so you don’t need to use an ornament to create these components. For developer guidance, see [Toolbars](/documentation/SwiftUI/Toolbars)
 and [`TabView`](/documentation/SwiftUI/TabView)
.

[Platform considerations](/design/human-interface-guidelines/ornaments#Platform-considerations)
-----------------------------------------------------------------------------------------------

*Not supported in iOS, iPadOS, macOS, tvOS, or watchOS.*

[Resources](/design/human-interface-guidelines/ornaments#Resources)
-------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/ornaments#Related)

[Layout](/design/human-interface-guidelines/layout)


#### [Developer documentation](/design/human-interface-guidelines/ornaments#Developer-documentation)

[`ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`](/documentation/SwiftUI/View/ornament(visibility:attachmentAnchor:contentAlignment:ornament:))


#### [Videos](/design/human-interface-guidelines/ornaments#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/38E4EE32-29B5-4478-B8B6-35B8ACA67B16/8130_wide_250x141_1x.jpg) Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_1x.jpg) Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072) 
[Change log](/design/human-interface-guidelines/ornaments#Change-log)
---------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | New page. |

