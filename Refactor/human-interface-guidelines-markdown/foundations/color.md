Updated to include guidance for visionOS. Color
=====

Judicious use of color can enhance communication, evoke your brand, provide visual continuity, communicate status and feedback, and help people understand information.![A sketch of a paint palette, suggesting the use of color. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/10ec5551985c77cabaeaaaff016cdfd8/foundations-color-intro@2x.png)

The system defines colors that look good on various backgrounds and appearance modes, and can automatically adapt to vibrancy and accessibility settings. People are familiar with the system colors, and using them is a convenient way to make your experience feel at home on the device.

You may also want to use custom colors to enhance the visual experience of your app or game and express its unique personality. The following guidelines can help you use color in ways that people appreciate, regardless of whether you use system-defined or custom colors.

[Best practices](/design/human-interface-guidelines/color#Best-practices)
-------------------------------------------------------------------------

**Use color sparingly in nongame apps.** In a nongame app, overuse of color can make communication less clear and can distract people. Prefer using touches of color to call attention to important information or show the relationship between parts of the interface.

**Avoid using the same color to mean different things.** Use color consistently throughout your interface, especially when you use it to help communicate information like status or interactivity. For example, an app might use blue to indicate that people can tap text to view more. Even when the app communicates interactivity using a visual indicator that doesn’t rely on color — such as a chevron or arrow icon — using a color other than blue for the interactive text is confusing.

**Make sure your app’s colors work well in both light and dark contexts.** Most platforms offer a dark alternative to the default light appearance called [Dark Mode](/design/human-interface-guidelines/dark-mode)
. Dark Mode uses a darker color palette for all screens, views, menus, and controls, and can increase *vibrancy* — a subtle effect that dynamically blends foreground and background colors — to make foreground content stand out against darker backgrounds (for guidance, see [Materials](/design/human-interface-guidelines/materials)
). Instead of offering Dark Mode, watchOS always uses a pure black background, and visionOS uses a material called glass that automatically adapts to the luminance of the surrounding objects and colors. In all platforms, system colors automatically support light and dark contexts as needed; if you use a custom color, you need to supply both variants.

**Test your app’s color scheme under a variety of lighting conditions.** For example, colors can look different when you run your app outside on a sunny day or in dim light. In visionOS, colors can look different depending on the colors of a wall or object in a person’s physical surroundings and how it reflects light. Adjust app colors to provide an optimal viewing experience in the majority of use cases.

**Test your app on different devices.** For example, the True Tone display — available on certain iPhone, iPad, and Mac models — uses ambient light sensors to automatically adjust the white point of the display to adapt to the lighting conditions of the current environment. Apps that focus primarily on reading, photos, video, and gaming can strengthen or weaken this effect by specifying a white point adaptivity style (for developer guidance, see [`UIWhitePointAdaptivityStyle`](/documentation/bundleresources/information_property_list/uiwhitepointadaptivitystyle)
). Test tvOS apps on multiple brands of HD and 4K TVs, and with different display settings. You can also test the appearance of your app using different color profiles on a Mac — such as P3 and Standard RGB (sRGB) — by choosing a profile in System Settings > Displays. For guidance, see [Color management](/design/human-interface-guidelines/color#Color-management)
.

**Consider how artwork and translucency affect nearby colors.** Variations in artwork sometimes warrant changes to nearby colors to maintain visual continuity and prevent interface elements from becoming overpowering or underwhelming. Maps, for example, displays a light color scheme when in map mode but switches to a dark color scheme when in satellite mode. Colors can also appear different when placed behind or applied to a translucent element like a toolbar.

**If your app lets people choose colors, prefer system-provided color controls where available.** Using built-in color pickers provides a consistent user experience, in addition to letting people save a set of colors they can access from any app. For developer guidance, see [`ColorPicker`](/documentation/SwiftUI/ColorPicker)
.

[Inclusive color](/design/human-interface-guidelines/color#Inclusive-color)
---------------------------------------------------------------------------

**Avoid relying solely on color to differentiate between objects, indicate interactivity, or communicate essential information.** When you use color to convey information, be sure to provide the same information in alternative ways so people with color blindness or other visual disabilities can understand it. For example, you can use labels or glyph shapes to identify objects or states.

**Avoid using colors that make it hard to perceive content in your app.** For example, insufficient contrast can cause icons and text to blend with the background and make content hard to read, and people who are color blind might not be able to distinguish some color combinations. For guidance, see [Color and effects](/design/human-interface-guidelines/accessibility#Color-and-effects)
.

**Consider how the colors you use might be perceived in other countries and cultures.** For example, red communicates danger in some cultures, but has positive connotations in other cultures. Make sure the colors in your app send the message you intend.

[System colors](/design/human-interface-guidelines/color#System-colors)
-----------------------------------------------------------------------

**Avoid hard-coding system color values in your app.** Documented color values are for your reference during the app design process. The actual color values may fluctuate from release to release, based on a variety of environmental variables. Use APIs like [`Color`](/documentation/SwiftUI/Color)
 to apply system colors.

iOS, iPadOS, macOS, and visionOS also define sets of *dynamic system colors* that match the color schemes of standard UI components and automatically adapt to both light and dark contexts. Each dynamic color is semantically defined by its purpose, rather than its appearance or color values. For example, some colors represent view backgrounds at different levels of hierarchy and other colors represent foreground content, such as labels, links, and separators.

**Avoid replicating dynamic system colors.** Dynamic system colors — some of which can be patterns — may fluctuate from release to release, based on a variety of environmental variables.

**Avoid redefining the semantic meanings of dynamic system colors.** To ensure a consistent experience and ensure your interface looks great when the appearance of the platform changes, use dynamic system colors as intended.

[Color management](/design/human-interface-guidelines/color#Color-management)
-----------------------------------------------------------------------------

A *color space* represents the colors in a *color model* like RGB or CMYK. Common color spaces — sometimes called *gamuts* — are sRGB and Display P3.

![Diagram showing the colors included in the sRGB space, compared to the larger number of colors included in the P3 color space.](https://docs-assets.developer.apple.com/published/080494c70f63b88c8646f75aad962673/color-graphic-wide-color@2x.png)

A *color profile* describes the colors in a color space using, for example, mathematical formulas or tables of data that map colors to numerical representations. An image embeds its color profile so that a device can interpret the image’s colors correctly and reproduce them on a display.

**Apply color profiles to your images.** Color profiles help ensure that your app’s colors appear as intended on different displays. The sRGB color space produces accurate colors on most displays.

**Use wide color to enhance the visual experience on compatible displays.** Wide color displays support a P3 color space, which can produce richer, more saturated colors than sRGB. As a result, photos and videos that use wide color are more lifelike, and visual data and status indicators that use wide color can be more meaningful. When appropriate, use the Display P3 color profile at 16 bits per pixel (per channel) and export images in PNG format. Note that you need to use a wide color display to design wide color images and select P3 colors.

**Provide color space–specific image and color variations if necessary.** In general, P3 colors and images appear fine on sRGB displays. Occasionally, it may be hard to distinguish two very similar P3 colors when viewing them on an sRGB display. Gradients that use P3 colors can also sometimes appear clipped on sRGB displays. To avoid these issues and to ensure visual fidelity on both wide color and sRGB displays, you can use the asset catalog of your Xcode project to provide different versions of images and colors for each color space.

To learn more, see [How to start designing assets in Display P3](https://developer.apple.com/news/?id=5cda5ipr)
.

[Platform considerations](/design/human-interface-guidelines/color#Platform-considerations)
-------------------------------------------------------------------------------------------

### [iOS, iPadOS](/design/human-interface-guidelines/color#iOS-iPadOS)

iOS defines two sets of dynamic background colors — *system* and *grouped* — each of which contains primary, secondary, and tertiary variants that help you convey a hierarchy of information. In general, use the grouped background colors ([`systemGroupedBackground`](/documentation/uikit/uicolor/3173145-systemgroupedbackground)
, [`secondarySystemGroupedBackground`](/documentation/uikit/uicolor/3173138-secondarysystemgroupedbackground)
, and [`tertiarySystemGroupedBackground`](/documentation/uikit/uicolor/3173155-tertiarysystemgroupedbackground)
) when you have a grouped table view; otherwise, use the system set of background colors ([`systemBackground`](/documentation/uikit/uicolor/3173140-systembackground)
, [`secondarySystemBackground`](/documentation/uikit/uicolor/3173137-secondarysystembackground)
, and [`tertiarySystemBackground`](/documentation/uikit/uicolor/3173154-tertiarysystembackground)
).

With both sets of background colors, you generally use the variants to indicate hierarchy in the following ways:

* Primary for the overall view
* Secondary for grouping content or elements within the overall view
* Tertiary for grouping content or elements within secondary elements

For foreground content, iOS defines the following dynamic colors:



| Color | Use for… | UIKit API |
| --- | --- | --- |
| Label | A text label that contains primary content. | [`label`](/documentation/uikit/uicolor/3173131-label)
 |
| Secondary label | A text label that contains secondary content. | [`secondaryLabel`](/documentation/uikit/uicolor/3173136-secondarylabel)
 |
| Tertiary label | A text label that contains tertiary content. | [`tertiaryLabel`](/documentation/uikit/uicolor/3173153-tertiarylabel)
 |
| Quaternary label | A text label that contains quaternary content. | [`quaternaryLabel`](/documentation/uikit/uicolor/3173135-quaternarylabel)
 |
| Placeholder text | Placeholder text in controls or text views. | [`placeholderText`](/documentation/uikit/uicolor/3173134-placeholdertext)
 |
| Separator | A separator that allows some underlying content to be visible. | [`separator`](/documentation/uikit/uicolor/3173139-separator)
 |
| Opaque separator | A separator that doesn’t allow any underlying content to be visible. | [`opaqueSeparator`](/documentation/uikit/uicolor/3173133-opaqueseparator)
 |
| Link | Text that functions as a link. | [`link`](/documentation/uikit/uicolor/3173132-link)
 |

### [macOS](/design/human-interface-guidelines/color#macOS)

macOS defines the following dynamic system colors (you can also view them in the Developer palette of the standard Color panel):



| Color | Use for… | AppKit API |
| --- | --- | --- |
| Alternate selected control text color | The text on a selected surface in a list or table. | [`alternateSelectedControlTextColor`](/documentation/appkit/nscolor/1527413-alternateselectedcontroltextcolo)
 |
| Alternating content background colors | The backgrounds of alternating rows or columns in a list, table, or collection view. | [`alternatingContentBackgroundColors`](/documentation/appkit/nscolor/2998825-alternatingcontentbackgroundcolo)
 |
| Control accent | The accent color people select in System Settings. | [`controlAccentColor`](/documentation/appkit/nscolor/3000782-controlaccentcolor)
 |
| Control background color | The background of a large interface element, such as a browser or table. | [`controlBackgroundColor`](/documentation/appkit/nscolor/1531948-controlbackgroundcolor)
 |
| Control color | The surface of a control. | [`controlColor`](/documentation/appkit/nscolor/1524856-controlcolor)
 |
| Control text color | The text of a control that is available. | [`controlTextColor`](/documentation/appkit/nscolor/1535230-controltextcolor)
 |
| Current control tint | The system-defined control tint. | [`currentControlTint`](/documentation/appkit/nscolor/1526377-currentcontroltint)
 |
| Unavailable control text color | The text of a control that’s unavailable. | [`disabledControlTextColor`](/documentation/appkit/nscolor/1530573-disabledcontroltextcolor)
 |
| Find highlight color | The color of a find indicator. | [`findHighlightColor`](/documentation/appkit/nscolor/2998827-findhighlightcolor)
 |
| Grid color | The gridlines of an interface element, such as a table. | [`gridColor`](/documentation/appkit/nscolor/1527240-gridcolor)
 |
| Header text color | The text of a header cell in a table. | [`headerTextColor`](/documentation/appkit/nscolor/1531237-headertextcolor)
 |
| Highlight color | The virtual light source onscreen. | [`highlightColor`](/documentation/appkit/nscolor/1527697-highlightcolor)
 |
| Keyboard focus indicator color | The ring that appears around the currently focused control when using the keyboard for interface navigation. | [`keyboardFocusIndicatorColor`](/documentation/appkit/nscolor/1532031-keyboardfocusindicatorcolor)
 |
| Label color | The text of a label containing primary content. | [`labelColor`](/documentation/appkit/nscolor/1534657-labelcolor)
 |
| Link color | A link to other content. | [`linkColor`](/documentation/appkit/nscolor/2998828-linkcolor)
 |
| Placeholder text color | A placeholder string in a control or text view. | [`placeholderTextColor`](/documentation/appkit/nscolor/2998829-placeholdertextcolor)
 |
| Quaternary label color | The text of a label of lesser importance than a tertiary label, such as watermark text. | [`quaternaryLabelColor`](/documentation/appkit/nscolor/1534635-quaternarylabelcolor)
 |
| Scrubber textured background color | The background of a scrubber in the Touch Bar. For guidance, see [Touch Bar](/design/human-interface-guidelines/touch-bar)
. | [`scrubberTexturedBackgroundColor`](/documentation/appkit/nscolor/2646931-scrubbertexturedbackgroundcolor)
 |
| Secondary label color | The text of a label of lesser importance than a primary label, such as a label used to represent a subheading or additional information. | [`secondaryLabelColor`](/documentation/appkit/nscolor/1533254-secondarylabelcolor)
 |
| Selected content background color | The background for selected content in a key window or view. | [`selectedContentBackgroundColor`](/documentation/appkit/nscolor/2998830-selectedcontentbackgroundcolor)
 |
| Selected control color | The surface of a selected control. | [`selectedControlColor`](/documentation/appkit/nscolor/1526796-selectedcontrolcolor)
 |
| Selected control text color | The text of a selected control. | [`selectedControlTextColor`](/documentation/appkit/nscolor/1535591-selectedcontroltextcolor)
 |
| Selected menu item text color | The text of a selected menu. | [`selectedMenuItemTextColor`](/documentation/appkit/nscolor/1526658-selectedmenuitemtextcolor)
 |
| Selected text background color | The background of selected text. | [`selectedTextBackgroundColor`](/documentation/appkit/nscolor/1528136-selectedtextbackgroundcolor)
 |
| Selected text color | The color for selected text. | [`selectedTextColor`](/documentation/appkit/nscolor/1528605-selectedtextcolor)
 |
| Separator color | A separator between different sections of content. | [`separatorColor`](/documentation/appkit/nscolor/2998831-separatorcolor)
 |
| Shadow color | The virtual shadow cast by a raised object onscreen. | [`shadowColor`](/documentation/appkit/nscolor/1525121-shadowcolor)
 |
| Tertiary label color | The text of a label of lesser importance than a secondary label. | [`tertiaryLabelColor`](/documentation/appkit/nscolor/1532376-tertiarylabelcolor)
 |
| Text background color | The background color behind text. | [`textBackgroundColor`](/documentation/appkit/nscolor/1535446-textbackgroundcolor)
 |
| Text color | The text in a document. | [`textColor`](/documentation/appkit/nscolor/1527025-textcolor)
 |
| Under page background color | The background behind a document’s content. | [`underPageBackgroundColor`](/documentation/appkit/nscolor/1534707-underpagebackgroundcolor)
 |
| Unemphasized selected content background color | The selected content in a non-key window or view. | [`unemphasizedSelectedContentBackgroundColor`](/documentation/appkit/nscolor/2998832-unemphasizedselectedcontentbackg)
 |
| Unemphasized selected text background color | A background for selected text in a non-key window or view. | [`unemphasizedSelectedTextBackgroundColor`](/documentation/appkit/nscolor/2998833-unemphasizedselectedtextbackgrou)
 |
| Unemphasized selected text color | Selected text in a non-key window or view. | [`unemphasizedSelectedTextColor`](/documentation/appkit/nscolor/2998834-unemphasizedselectedtextcolor)
 |
| Window background color | The background of a window. | [`windowBackgroundColor`](/documentation/appkit/nscolor/1528630-windowbackgroundcolor)
 |
| Window frame text color | The text in the window’s title bar area. | [`windowFrameTextColor`](/documentation/appkit/nscolor/1524257-windowframetextcolor)
 |

#### [App accent colors](/design/human-interface-guidelines/color#App-accent-colors)

Beginning in macOS 11, you can specify an *accent color* to customize the appearance of your app’s buttons, selection highlighting, and sidebar icons. The system applies your accent color when the current value in General > Accent color settings is *multicolor*.

![A screenshot of a window that includes a sidebar. Each item in the sidebar displays an icon at its leading edge. Each icon uses the purple accent color.](https://docs-assets.developer.apple.com/published/4d928abfd24f75ed7f73186da65acff4/app-accent-colors-podcasts@2x.png)

![A screenshot of a window that includes a toolbar. The purple accent color is visible in the currently selected toolbar icon and in the content area's pop-up buttons.](https://docs-assets.developer.apple.com/published/afba54f2945b14a235f5e49125339be2/app-accent-colors-podcasts-preferences@2x.png)

If people set their accent color setting to a value other than multicolor, the system applies their chosen color to the relevant items throughout your app, replacing your accent color. The exception is a sidebar icon that uses a fixed color you specify. Because a fixed-color sidebar icon uses a specific color to provide meaning, the system doesn’t override its color when people change the value of accent color settings. For guidance, see [Sidebars](/design/human-interface-guidelines/sidebars)
.

![A screenshot of a window that includes a sidebar.](https://docs-assets.developer.apple.com/published/f76d78192622b89754e5ea0058327ec3/fixed-color-orange@2x.png)The iCloud icon remains blue, even when the other glyphs use orange.### [tvOS](/design/human-interface-guidelines/color#tvOS)

**Consider choosing a limited color palette that coordinates with your app logo.** Subtle use of color can help you communicate your brand while deferring to the content.

**Avoid using only color to indicate focus.** Subtle scaling and responsive animation are the primary ways to denote interactivity when an element is in focus.

### [visionOS](/design/human-interface-guidelines/color#visionOS)

**Use color sparingly, especially on glass.** Standard visionOS windows typically use the system-defined glass [material](/design/human-interface-guidelines/materials)
, which lets light and objects from people’s physical surroundings and their space show through. Because the colors in these physical and virtual objects are visible through the glass, they can affect the legibility of colorful app content in the window. Prefer using color in places where it can help call attention to important information or show the relationship between parts of the interface.

**Prefer using color in bold text and large areas.** Color in lightweight text or small areas can make them harder to see and understand.

### [watchOS](/design/human-interface-guidelines/color#watchOS)

**Use background color to support existing content or supply additional information.** Background color can establish a sense of place and help people recognize key content. For example, in Activity, each infographic view for the Move, Exercise, and Stand Activity rings has a background that matches the color of the ring on which the person is focused. Use background color when you have something to communicate, rather than as a solely visual flourish.

**Recognize that people might prefer graphic complications to use tinted mode instead of full color.** The system can use a single color that’s based on the wearer’s selected color in a graphic complication’s images, gauges, and text. For guidance, see [Complications](/design/human-interface-guidelines/complications)
.

[Specifications](/design/human-interface-guidelines/color#Specifications)
-------------------------------------------------------------------------

### [iOS, iPadOS system colors](/design/human-interface-guidelines/color#iOS-iPadOS-system-colors)



| Name | SwiftUI API | Default (Light) | Default (Dark) | Accessible (Light) | Accessible (Dark) |
| --- | --- | --- | --- | --- | --- |
| Red | [`red`](/documentation/SwiftUI/Color/red)
 | R-255,G-59,B-48 | R-255,G-69,B-58 | R-215,G-0,B-21 | R-255,G-105,B-97 |
| Orange | [`orange`](/documentation/SwiftUI/Color/orange)
 | R-255,G-149,B-0 | R-255,G-159,B-10 | R-201,G-52,B-0 | R-255,G-179,B-64 |
| Yellow | [`yellow`](/documentation/SwiftUI/Color/yellow)
 | R-255,G-204,B-0 | R-255,G-214,B-10 | R-178,G-80,B-0 | R-255,G-212,B-38 |
| Green | [`green`](/documentation/SwiftUI/Color/green)
 | R-52,G-199,B-89 | R-48,G-209,B-88 | R-36,G-138,B-61 | R-48,G-219,B-91 |
| Mint | [`mint`](/documentation/SwiftUI/Color/mint)
 | R-0,G-199,B-190 | R-102,G-212,B-207 | R-12,G-129,B-123 | R-102,G-212,B-207 |
| Teal | [`teal`](/documentation/SwiftUI/Color/teal)
 | R-48,G-176,B-199 | R-64,G-200,B-224 | R-0,G-130,B-153 | R-93,G-230,B-255 |
| Cyan | [`cyan`](/documentation/SwiftUI/Color/cyan)
 | R-50,G-173,B-230 | R-100,G-210,B-255 | R-0,G-113,B-164 | R-112,G-215,B-255 |
| Blue | [`blue`](/documentation/SwiftUI/Color/blue)
 | R-0,G-122,B-255 | R-10,G-132,B-255 | R-0,G-64,B-221 | R-64,G-156,B-255 |
| Indigo | [`indigo`](/documentation/SwiftUI/Color/indigo)
 | R-88,G-86,B-214 | R-94,G-92,B-230 | R-54,G-52,B-163 | R-125,G-122,B-255 |
| Purple | [`purple`](/documentation/SwiftUI/Color/purple)
 | R-175,G-82,B-222 | R-191,G-90,B-242 | R-137,G-68,B-171 | R-218,G-143,B-255 |
| Pink | [`pink`](/documentation/SwiftUI/Color/pink)
 | R-255,G-45,B-85 | R-255,G-55,B-95 | R-211,G-15,B-69 | R-255,G-100,B-130 |
| Brown | [`brown`](/documentation/SwiftUI/Color/brown)
 | R-165,G-132,B-94 | R-172,G-142,B-104 | R-127,G-101,B-69 | R-181,G-148,B-105 |

### [iOS, iPadOS system gray colors](/design/human-interface-guidelines/color#iOS-iPadOS-system-gray-colors)



| Name | SwiftUI API | Default (Light) | Default (Dark) | Accessible (Light) | Accessible (Dark) |
| --- | --- | --- | --- | --- | --- |
| Gray | [`gray`](/documentation/SwiftUI/Color/gray)
 | R-142,G-142,B-147 | R-142,G-142,B-147 | R-108,G-108,B-112 | R-174,G-174,B-178 |
| Gray (2) | [`systemGray2`](/documentation/uikit/uicolor/3255071-systemgray2)
 | R-174,G-174,B-178 | R-99,G-99,B-102 | R-142,G-142,B-147 | R-124,G-124,B-128 |
| Gray (3) | [`systemGray3`](/documentation/uikit/uicolor/3255072-systemgray3)
 | R-199,G-199,B-204 | R-72,G-72,B-74 | R-174,G-174,B-178 | R-84,G-84,B-86 |
| Gray (4) | [`systemGray4`](/documentation/uikit/uicolor/3255073-systemgray4)
 | R-209,G-209,B-214 | R-58,G-58,B-60 | R-188,G-188,B-192 | R-68,G-68,B-70 |
| Gray (5) | [`systemGray5`](/documentation/uikit/uicolor/3255074-systemgray5)
 | R-229,G-229,B-234 | R-44,G-44,B-46 | R-216,G-216,B-220 | R-54,G-54,B-56 |
| Gray (6) | [`systemGray6`](/documentation/uikit/uicolor/3255075-systemgray6)
 | R-242,G-242,B-247 | R-28,G-28,B-30 | R-235,G-235,B-240 | R-36,G-36,B-38 |

### [macOS system colors](/design/human-interface-guidelines/color#macOS-system-colors)

* [Default](#)
* [Vibrant](#)


| Name | SwiftUI API | Default (Light) | Default (Dark) | Accessible (Light) | Accessible (Dark) |
| --- | --- | --- | --- | --- | --- |
| Red | [`red`](/documentation/SwiftUI/Color/red)
 | R-255,G-59,B-48 | R-255,G-69,B-58 | R-215,G-0,B-21 | R-255,G-105,B-97 |
| Orange | [`orange`](/documentation/SwiftUI/Color/orange)
 | R-255,G-149,B-0 | R-255,G-159,B-10 | R-201,G-52,B-0 | R-255,G-179,B-64 |
| Yellow | [`yellow`](/documentation/SwiftUI/Color/yellow)
 | R-255,G-204,B-0 | R-255,G-214,B-10 | R-160,G-90,B-0 | R-255,G-212,B-38 |
| Green | [`green`](/documentation/SwiftUI/Color/green)
 | R-40,G-205,B-65 | R-50,G-215,B-75 | R-0,G-125,B-27 | R-49,G-222,B-75 |
| Mint | [`mint`](/documentation/SwiftUI/Color/mint)
 | R-0,G-199,B-190 | R-102,G-212,B-207 | R-12,G-129,B-123 | R-102,G-212,B-207 |
| Teal | [`teal`](/documentation/SwiftUI/Color/teal)
 | R-89,G-173,B-196 | R-106,G-196,B-220 | R-0,G-130,B-153 | R-93,G-230,B-255 |
| Cyan | [`cyan`](/documentation/SwiftUI/Color/cyan)
 | R-85,G-190,B-240 | R-90,G-200,B-245 | R-0,G-113,B-164 | R-112,G-215,B-255 |
| Blue | [`blue`](/documentation/SwiftUI/Color/blue)
 | R-0,G-122,B-255 | R-10,G-132,B-255 | R-0,G-64,B-221 | R-64,G-156,B-255 |
| Indigo | [`indigo`](/documentation/SwiftUI/Color/indigo)
 | R-88,G-86,B-214 | R-94,G-92,B-230 | R-54,G-52,B-163 | R-125,G-122,B-255 |
| Purple | [`purple`](/documentation/SwiftUI/Color/purple)
 | R-175,G-82,B-222 | R-191,G-90,B-242 | R-173,G-68,B-171 | R-218,G-143,B-255 |
| Pink | [`pink`](/documentation/SwiftUI/Color/pink)
 | R-255,G-45,B-85 | R-255,G-55,B-95 | R-211,G-15,B-69 | R-255,G-100,B-130 |
| Brown | [`brown`](/documentation/SwiftUI/Color/brown)
 | R-162,G-132,B-94 | R-172,G-142,B-104 | R-127,G-101,B-69 | R-181,G-148,B-105 |
| Gray | [`gray`](/documentation/SwiftUI/Color/gray)
 | R-142,G-142,B-147 | R-152,G-152,B-157 | R-105,G-105,B-110 | R-152,G-152,B-157 |



| Name | SwiftUI API | Default (Light) | Default (Dark) | Accessible (Light) | Accessible (Dark) |
| --- | --- | --- | --- | --- | --- |
| Red | [`red`](/documentation/SwiftUI/Color/red)
 | R-255,G-49,B-38 | R-255,G-79,B-68 | R-194,G-6,B-24 | R-255,G-65,B-54 |
| Orange | [`orange`](/documentation/SwiftUI/Color/orange)
 | R-245,G-139,B-0 | R-255,G-169,B-20 | R-173,G-58,B-0 | R-255,G-179,B-64 |
| Yellow | [`yellow`](/documentation/SwiftUI/Color/yellow)
 | R-245,G-194,B-0 | R-255,G-169,B-20 | R-146,G-81,B-0 | R-255,G-212,B-38 |
| Green | [`green`](/documentation/SwiftUI/Color/green)
 | R-30,G-195,B-55 | R-60,G-225,B-85 | R-0,G-112,B-24 | R-49,G-222,B-75 |
| Mint | [`mint`](/documentation/SwiftUI/Color/mint)
 | R-0,G-189,B-180 | R-108,G-224,B-219 | R-11,G-117,B-112 | R-102,G-212,B-207 |
| Teal | [`teal`](/documentation/SwiftUI/Color/teal)
 | R-46,G-167,B-189 | R-68,G-212,B-237 | R-0,G-119,B-140 | R-93,G-230,B-255 |
| Cyan | [`cyan`](/documentation/SwiftUI/Color/cyan)
 | R-65,G-175,B-220 | R-90,G-205,B-250 | R-0,G-103,B-150 | R-112,G-215,B-255 |
| Blue | [`blue`](/documentation/SwiftUI/Color/blue)
 | R-0,G-112,B-245 | R-20,G-142,B-255 | R-0,G-64,B-221 | R-64,G-156,B-255 |
| Indigo | [`indigo`](/documentation/SwiftUI/Color/indigo)
 | R-84,G-82,B-204 | R-99,G-97,B-242 | R-54,G-52,B-163 | R-125,G-122,B-255 |
| Purple | [`purple`](/documentation/SwiftUI/Color/purple)
 | R-159,G-75,B-201 | R-204,G-101,B-255 | R-173,G-68,B-171 | R-218,G-143,B-255 |
| Pink | [`pink`](/documentation/SwiftUI/Color/pink)
 | R-245,G-35,B-75 | R-255,G-65,B-105 | R-193,G-16,B-50 | R-255,G-58,B-95 |
| Brown | [`brown`](/documentation/SwiftUI/Color/brown)
 | R-152,G-122,B-84 | R-182,G-152,B-114 | R-119,G-93,B-59 | R-181,G-148,B-105 |
| Gray | [`gray`](/documentation/SwiftUI/Color/gray)
 | R-132,G-132,B-137 | R-162,G-162,B-167 | R-97,G-97,B-101 | R-152,G-152,B-157 |

### [visionOS system colors](/design/human-interface-guidelines/color#visionOS-system-colors)



| Name | SwiftUI API | Default |
| --- | --- | --- |
| Red | [`red`](/documentation/SwiftUI/Color/red)
 | R-255,G-69,B-58 |
| Orange | [`orange`](/documentation/SwiftUI/Color/orange)
 | R-255,G-159,B-10 |
| Yellow | [`yellow`](/documentation/SwiftUI/Color/yellow)
 | R-255,G-214,B-10 |
| Green | [`green`](/documentation/SwiftUI/Color/green)
 | R-50,G-215,B-75 |
| Mint | [`mint`](/documentation/SwiftUI/Color/mint)
 | R-102,G-212,B-207 |
| Teal | [`teal`](/documentation/SwiftUI/Color/teal)
 | R-106,G-196,B-220 |
| Cyan | [`cyan`](/documentation/SwiftUI/Color/cyan)
 | R-90,G-200,B-245 |
| Blue | [`blue`](/documentation/SwiftUI/Color/blue)
 | R-10,G-132,B-255 |
| Indigo | [`indigo`](/documentation/SwiftUI/Color/indigo)
 | R-94,G-92,B-230 |
| Purple | [`purple`](/documentation/SwiftUI/Color/purple)
 | R-191,G-90,B-242 |
| Pink | [`pink`](/documentation/SwiftUI/Color/pink)
 | R-255,G-55,B-95 |
| Brown | [`brown`](/documentation/SwiftUI/Color/brown)
 | R-172,G-142,B-104 |
| Gray | [`gray`](/documentation/SwiftUI/Color/gray)
 | R-152,G-152,B-157 |

### [watchOS system colors](/design/human-interface-guidelines/color#watchOS-system-colors)



| Name | SwiftUI API | Default (Light) | Default (Dark) | Accessible (Light) | Accessible (Dark) |
| --- | --- | --- | --- | --- | --- |
| Red | [`red`](/documentation/SwiftUI/Color/red)
 | R-246,G-52,B-40 | R-255,G-59,B-48 | R-215,G-0,B-21 | R-255,G-105,B-97 |
| Orange | [`orange`](/documentation/SwiftUI/Color/orange)
 | R-255,G-140,B-0 | R-255,G-149,B-0 | R-177,G-90,B-0 | R-255,G-179,B-64 |
| Yellow | [`yellow`](/documentation/SwiftUI/Color/yellow)
 | R-255,G-204,B-0 | R-255,G-214,B-10 | R-143,G-116,B-0 | R-255,G-242,B-97 |
| Green | [`green`](/documentation/SwiftUI/Color/green)
 | R-2,G-212,B-106 | R-4,G-222,B-113 | R-0,G-134,B-74 | R-12,G-255,B-134 |
| Mint | [`mint`](/documentation/SwiftUI/Color/mint)
 | R-0,G-199,B-190 | R-0,G-245,B-234 | R-12,G-129,B-123 | R-108,G-255,B-249 |
| Teal | [`teal`](/documentation/SwiftUI/Color/teal)
 | R-48,G-176,B-199 | R-64,G-200,B-224 | R-0,G-130,B-153 | R-93,G-230,B-255 |
| Cyan | [`cyan`](/documentation/SwiftUI/Color/cyan)
 | R-50,G-173,B-230 | R-90,G-200,B-250 | R-0,G-113,B-164 | R-112,G-215,B-255 |
| Blue | [`blue`](/documentation/SwiftUI/Color/blue)
 | R-0,G-122,B-255 | R-32,G-148,B-250 | R-0,G-64,B-221 | R-90,G-168,B-255 |
| Indigo | [`indigo`](/documentation/SwiftUI/Color/indigo)
 | R-88,G-86,B-214 | R-120,G-122,B-255 | R-54,G-52,B-163 | R-155,G-153,B-255 |
| Purple | [`purple`](/documentation/SwiftUI/Color/purple)
 | R-175,G-82,B-222 | R-191,G-90,B-242 | R-137,G-68,B-171 | R-218,G-143,B-255 |
| Pink | [`pink`](/documentation/SwiftUI/Color/pink)
 | R-234,G-14,B-74 | R-250,G-17,B-79 | R-211,G-15,B-69 | R-255,G-100,B-130 |
| Brown | [`brown`](/documentation/SwiftUI/Color/brown)
 | R-162,G-132,B-94 | R-172,G-142,B-104 | R-127,G-101,B-69 | R-219,G-178,B-124 |

[Resources](/design/human-interface-guidelines/color#Resources)
---------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/color#Related)

[Dark Mode](/design/human-interface-guidelines/dark-mode)


[Accessibility](/design/human-interface-guidelines/accessibility)


#### [Developer documentation](/design/human-interface-guidelines/color#Developer-documentation)

[`Color`](/documentation/SwiftUI/Color)


[UI element colors](/documentation/uikit/uicolor/ui_element_colors)


#### [Videos](/design/human-interface-guidelines/color#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/48/0F960683-D91F-4CA9-9658-6FBB11F0683D/3272_wide_250x141_1x.jpg) What's New in iOS Design](https://developer.apple.com/videos/play/wwdc2019/808) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/7/09438FDD-3E8B-42A3-A364-78E1A7F2CE6B/1915_wide_250x141_1x.jpg) Get Started with Display P3](https://developer.apple.com/videos/play/wwdc2017/821) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/48/174747D6-8723-4194-A932-7765179F1108/2949_wide_250x141_1x.jpg) Implementing Dark Mode on iOS](https://developer.apple.com/videos/play/wwdc2019/214) 
[Change log](/design/human-interface-guidelines/color#Change-log)
-----------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance for using background color in watchOS. |
| December 19, 2022 | Corrected RGB values for system mint color (Dark Mode) in iOS and iPadOS. |

