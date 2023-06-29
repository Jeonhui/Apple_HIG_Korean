June 21, 2023

 Updated to include guidance for visionOS. Segmented controls
==================

A segmented control is a linear set of two or more segments, each of which functions as a button.![A stylized representation of a selected segment in a segmented control. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4e70f0b4ae782303cabad93cc1ad25a4/components-segmented-control-intro@2x.png)

Within a segmented control, all segments are usually equal in width. Like buttons, segments can contain text or images. Segments can also have text labels beneath them (or beneath the control as a whole).

[Best practices](/design/human-interface-guidelines/segmented-controls#Best-practices)
--------------------------------------------------------------------------------------

A segmented control can offer a single choice or multiple choices. For example, in Keynote people can select only one segment in the alignment options control to align selected text. In contrast, people can choose multiple segments in the font attributes control to combine styles like bold, italics, and underline. The toolbar of a Keynote window also uses a segmented control to let people show and hide various editing panes within the main window area.

![A partial screenshot of a segmented control that consists of four text-alignment options. The center alignment option is selected.](https://docs-assets.developer.apple.com/published/8c06202270aa61dbeb3f3f76525c2cf2/segmented-control-one-choice@2x.png)Single choice![A partial screenshot of a segmented control that consists of four font types. Three of the four options are selected.](https://docs-assets.developer.apple.com/published/2da0fa7f757bf9a6332fa69b4c4f8514/segmented-control-multiple-choices@2x.png)Multiple choices**Use a segmented control to provide closely related choices that affect an object, state, or view.** For example, a segmented control can help people switch between views in a toolbar. Avoid using a segmented control to offer actions, such as adding, removing, or editing content.

**Avoid crowding the control with too many segments.** Too many segments can be hard to parse and time-consuming to navigate. Aim for no more than about five to seven segments in a wide interface and no more than about five segments on iPhone.

**In general, keep segment size consistent.** When all segments have equal width, a segmented control feels balanced. To the extent possible, it’s best to keep icon and title widths consistent too.

[Content](/design/human-interface-guidelines/segmented-controls#Content)
------------------------------------------------------------------------

**Prefer using either text or images — not a mix of both — in a single segmented control.** Although individual segments can contain text labels or images, mixing the two in a single control can lead to a disconnected and confusing interface.

**As much as possible, use content with a similar size in each segment.** Because all segments typically have equal width, it doesn’t look good if content fills some segments but not others.

**Use nouns or noun phrases for segment labels.** Write text that describes each segment and uses [title-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64)
. A segmented control that displays text labels doesn’t need introductory text.

[Platform considerations](/design/human-interface-guidelines/segmented-controls#Platform-considerations)
--------------------------------------------------------------------------------------------------------

*Not supported in watchOS.*

### [iOS, iPadOS](/design/human-interface-guidelines/segmented-controls#iOS-iPadOS)

**Use a segmented control in a bar only as recommended.** Specifically, if you use a segmented control in a navigation bar, avoid including any other controls or a title. Avoid using a segmented control in a toolbar, because toolbar items act on the current screen — they don’t let people switch contexts.

### [macOS](/design/human-interface-guidelines/segmented-controls#macOS)

**Consider using introductory text to clarify the purpose of a segmented control.** When the control uses symbols or interface icons, you could also add a label below each segment to clarify its meaning. If your app includes help tags, provide a help tag for each segment in a segmented control.

**Use a tab view in the main window area — instead of a segmented control — for view switching.** A [tab view](https://developer.apple.com/design/human-interface-guidelines/tab-views)
 supports efficient view switching and is similar in appearance to a [box](https://developer.apple.com/design/human-interface-guidelines/boxes)
 combined with a segmented control. Consider using a segmented control to help people switch views in a toolbar or inspector pane.

**Size custom interface icons appropriately based on the size of the control.** Use the following values for guidance.

![A partial screenshot of three regular-size icons in a regular-size segmented control.](https://docs-assets.developer.apple.com/published/983e3ff02ca8019fbdc26f270c729144/segmented-control-icons-regular@2x.png)Regular![A partial screenshot of three small-size icons in a small-size segmented control.](https://docs-assets.developer.apple.com/published/1d88d2369778727e3f09396ed8646280/segmented-control-icons-small@2x.png)Small![A partial screenshot of three mini-size icons in a mini-size segmented control.](https://docs-assets.developer.apple.com/published/7ad3599ca30edc73780b2dbea74821ba/segmented-control-icons-mini@2x.png)Mini

| Control size | Icon size |
| --- | --- |
| Regular | 17x17 px @1x (34x34 px @2x) |
| Small | 14x13 px @1x (28x26 px @2x) |
| Mini | 12x11 px @1x (24x22 px @2x) |

**Consider supporting spring loading.** On a Mac equipped with a Magic Trackpad, spring loading lets people activate a segment by dragging selected items over it and force clicking without dropping the selected items. People can also continue dragging the items after a segment activates.

### [tvOS](/design/human-interface-guidelines/segmented-controls#tvOS)

**Consider using a split view instead of a segmented control on screens that perform content filtering.** People generally find it easy to navigate back and forth between content and filtering options using a split view. Depending on its placement, a segmented control may not be as easy to access.

**Avoid putting other focusable elements close to segmented controls.** Segments become selected when focus moves to them, not when people click them. Carefully consider where you position a segmented control relative to other interface elements. If other focusable elements are too close, people might accidentally focus on them when attempting to switch between segments.

### [visionOS](/design/human-interface-guidelines/segmented-controls#visionOS)

When people bring focus to a segmented control that uses icons, the system displays a tooltip that contains the descriptive text you supply.

[Resources](/design/human-interface-guidelines/segmented-controls#Resources)
----------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/segmented-controls#Related)

[Split views](/design/human-interface-guidelines/split-views)


#### [Developer documentation](/design/human-interface-guidelines/segmented-controls#Developer-documentation)

[`segmented`](/documentation/SwiftUI/PickerStyle/segmented)


[`UISegmentedControl`](/documentation/uikit/uisegmentedcontrol)


[`NSSegmentedControl`](/documentation/appkit/nssegmentedcontrol)


[Change log](/design/human-interface-guidelines/segmented-controls#Change-log)
------------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |

