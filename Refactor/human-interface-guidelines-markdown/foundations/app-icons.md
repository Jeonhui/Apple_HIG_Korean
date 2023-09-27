Updated to include guidance for visionOS. App icons
=========

A unique, memorable icon communicates the purpose and personality of your app or game and can help people recognize your product at a glance in the App Store and on their devices.![A sketch of the App Store icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/05b8bbb4aac9f98ba8c77876fe5068b7/foundations-app-icons-intro@2x.png)

Beautiful app icons are an important part of the user experience on all Apple platforms and every app and game must have one. Each platform defines a slightly different style for app icons, so you want to create a design that adapts well to different shapes and levels of detail while maintaining strong visual consistency and messaging. To download templates that help you create icons for each platform, see [Apple Design Resources](https://developer.apple.com/design/resources/)
. For guidance on creating other types of icons, see [Icons](/design/human-interface-guidelines/icons)
.

[Best practices](/design/human-interface-guidelines/app-icons#Best-practices)
-----------------------------------------------------------------------------

**Embrace simplicity.** Simple icons tend to be easier for people to understand and recognize. Find a concept or element that captures the essence of your app or game, make it the focus point of the icon, and express it in a simple, unique way. Avoid adding too many details, because they can be hard to discern and can make an icon appear muddy, especially at smaller sizes. Prefer a simple background that puts the emphasis on the primary image — you don’t need to fill the entire icon with content.

**Create a design that works well on multiple platforms so that it feels at home on each.** If your app or game runs on more than one platform, use similar images and color palettes in all icons while rendering them in the style that’s appropriate for each platform. For example, in iOS and watchOS, the Safari app icon depicts the white and red compass needle on a blue background using a streamlined, graphical style; macOS displays the same elements, while adding shadow and detail, giving the compass a realistic weight and texture. Similarly, the Safari app icon in visionOS uses the same color scheme and content, but offers a true 3D appearance.

**Prefer including text only when it’s an essential part of your experience or brand.** Text in icons is often too small to read easily, can make an icon appear cluttered, and doesn’t support accessibility or localization. In some contexts, the app name appears near the icon, making it redundant to display the name within it. Although using a mnemonic like the first letter of your app’s name can help people recognize your app or game, avoid including nonessential words that tell people what to do with it — like “Watch” or “Play” — or context-specific terms like “New” or “For visionOS.”

**Prefer graphical images to photos and avoid replicating UI components in your icon.** Photos are full of details that don’t work well when viewed at small sizes. Instead of using a photo, create a graphic representation of the content that emphasizes the features you want people to notice. Similarly, if your app has an interface that people recognize, don’t just replicate standard UI components or use app screenshots in your icon.

**If needed, optimize your icon for the specific sizes the system displays in places like Spotlight search results, Settings, and notifications.** For iOS, iPadOS, and watchOS, you can tell Xcode to generate all sizes from your 1024×1024 px App Store icon, or you can provide assets for some or all individual icon sizes. For macOS and tvOS, you need to supply all sizes; for visionOS, you supply a single 1024x1024 px asset. If you create your own versions of your app icon, make sure the image remains distinct at all sizes. For example, you might remove fine details and unnecessary features, simplifying the image and exaggerating primary features. If you need to make such changes, keep them subtle so that your app icon remains visually consistent in every context.

![Two different sizes of the Safari app icon in macOS. The image on the left contains many more visual details than the image on the right.](https://docs-assets.developer.apple.com/published/347c224ae67d5fa2e1a19a328c4abf82/app-icon-sizes@2x.png)The 512x512 px Safari app icon (on the left) uses a circle of tick marks to indicate degrees; the 16x16 px version of the icon (on the right) doesn’t include this detail.**Design your icon as a full-bleed square image.** On most platforms, the system applies a mask that automatically adjusts icon corners to match the platform’s aesthetic. For example, visionOS and watchOS automatically apply a circular mask. Although the system applies the rounded rectangle appearance to the icon of an app created with Mac Catalyst, you need to create your macOS app icon in the correct rounded shape; for guidance, see [macOS](/design/human-interface-guidelines/app-icons#macOS)
. Note that for the layered app icons in [visionOS](/design/human-interface-guidelines/app-icons#visionOS)
 and [tvOS](/design/human-interface-guidelines/app-icons#tvOS)
, full-bleed content is best suited to the bottom layer. For downloadable production templates that help you create app icons for each platform, see [Apple Design Resources](https://developer.apple.com/design/resources/)
.

**Consider offering an alternate app icon.** In iOS, iPadOS, tvOS, and visionOS, people can choose an alternate version of an icon, which can strengthen their connection with the app or game and enhance their experience. For example, a sports app might offer different icons for different teams. Make sure that each alternate app icon you design remains closely related to your content and experience; avoid creating a version that people might mistake for the icon of a different app. When people want to switch to an alternate icon, they can visit your app’s settings.

Note

As with a primary app icon, alternate app icons are also subject to app review and must adhere to the [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/#design)
.

**Don’t use replicas of Apple hardware products.** Apple products are copyrighted and can’t be reproduced in your app icons.

[Platform considerations](/design/human-interface-guidelines/app-icons#Platform-considerations)
-----------------------------------------------------------------------------------------------

### [iOS, iPadOS](/design/human-interface-guidelines/app-icons#iOS-iPadOS)

**Don’t add an overlay or border to your Settings icon.** iOS automatically adds a 1-pixel stroke to all icons so that they look good on the white background of Settings.

### [macOS](/design/human-interface-guidelines/app-icons#macOS)

In macOS, app icons share a common set of visual attributes, including a rounded-rectangle shape, front-facing perspective, level position, and uniform drop shadow. Rooted in the macOS design language, these attributes showcase the lifelike rendering style people expect in macOS while presenting a harmonious user experience.

**Consider depicting a familiar tool to communicate what people use your app to do.** To give context to your app’s purpose, you can use the icon background to portray the tool’s environment or the items it affects. For example, the TextEdit icon pairs a mechanical pencil with a sheet of lined paper to suggest a utilitarian writing experience. After you create a detailed, realistic image of a tool, it often works well to let it float just above the background and extend slightly past the icon boundaries. If you do this, make sure the tool remains visually unified with the background and doesn’t overwhelm the rounded-rectangle shape.

![An image of the TextEdit icon, depicting white paper ruled with gray horizontal lines and one red vertical line that indicates the left margin. The icon is masked to a rounded rectangle shape and includes a realistic mechanical pencil that extends beyond the edges, slanting from top-right to bottom-left.](https://docs-assets.developer.apple.com/published/2aca727c561342c619be08ff00a201ab/app-icon-familiar-tool@2x.png)

**If you depict real objects in your app icon, make them look like they’re made of physical materials and have actual mass.** Consider replicating the characteristics of substances like fabric, glass, paper, and metal to convey an object’s weight and feel. For example, the Xcode app icon features a hammer that looks like it has a steel head and polymer grip.

![An image of the Xcode icon showing the capital letter A formed out of three cylinders outlined in white, surrounded by a white outlined circle. The circle and letter are shown on a blue rounded rectangle background. In front of the image is a realistic image of a claw hammer, slanting to the right and extending beyond the edges.](https://docs-assets.developer.apple.com/published/57b52f94a38308a4360b935fd9b4575b/app-icon-realistic-materials@2x.png)

**Use the drop shadow in the icon-design template.** The app-icon [template](https://developer.apple.com/design/resources/#macos-apps)
 includes the system-defined drop shadow that helps your app icon coordinate with other macOS icons.

**Consider using interior shadows and highlights to add definition and realism.** For example, the Mail app icon uses both shadows and highlights to give the envelope authenticity and to suggest that the flap is slightly open. In icons that include a tool that floats above a background — such as TextEdit or Xcode — interior shadows can strengthen the perception of depth and make the tool look real. Use shadows and highlights that suggest a light source facing the icon, positioned just above center and tilted slightly downward.

**Avoid defining contours that suggest a shape other than a rounded rectangle.** In rare cases, you might want to fine-tune the basic app icon shape, but doing so risks creating an icon that looks like it doesn’t belong in macOS. If you must alter the shape, prefer subtle adjustments that continue to express a rounded rectangle silhouette.

![An image of the Final Cut Pro X app icon, which is an idealized version of a clapperboard. The overall shape of the icon is a rounded rectangle, even though the arm of the clapperboard is raised slightly at the top.](https://docs-assets.developer.apple.com/published/4aec1dcfde11f119bc46155ade3aa933/app-icon-consistent-shape@2x.png)

**Keep primary content within the icon grid bounding box; keep all content within the outer bounding box.** If an icon’s primary content extends beyond the icon grid bounding box, it tends to look out of place. If you overlay a tool on your icon, it works well to align the tool’s top edge with the outer bounding box and its bottom edge with the inner bounding box, as shown below. You can use the grid to help you position items within an icon and to ensure that centered inner elements like circles use a size that’s consistent with other icons in the system.

![A diagram that shows various placement lines within a rounded rectangle shape. Centered in the diagram is a grid of horizontal and vertical lines, overlaid with three concentric circles and two diagonal lines. The outer boundary of the grid is a rounded rectangle labeled the icon grid bounding box. Outside the icon grid bounding box are two additional concentric rounded rectangles labeled the inner bounding box and outer bounding box. A long, narrow, shaded lozenge shape is on top of the grid, representing an approximate layout location for a tool. The tool shape extends from the inner bounding box to the outer bounding box, slanting from vertical at about 25 degrees to the right.](https://docs-assets.developer.apple.com/published/353174b1dba1274a8d43713b097862a5/app-icon-layout-guides@2x.png)

### [tvOS](/design/human-interface-guidelines/app-icons#tvOS)

tvOS app icons use between two and five layers to create a sense of depth and vitality as people bring them into focus. For guidance, see [Layered images](/design/human-interface-guidelines/images#Layered-images)
.

**Use appropriate layer separation.** If your icon includes a logo, separate the logo from the background. If your icon includes text, bring the text to the front so it’s not hidden by other layers when the parallax effect occurs.

![An image of the Apple TV System Settings app icon and images of five separate layers that comprise it.](https://docs-assets.developer.apple.com/published/5aa0e116e8fa0efc769df4c202fe70ff/icons-and-images-icon-structure@2x.png)

 [Play](#) 
**Use gradients and shadows cautiously.** Background gradients and vignettes can clash with the parallax effect. For gradients, prefer top-to-bottom, light-to-dark styles. Shadows usually look best as sharp, hard-edged tints that are baked into the background layer and aren’t visible when the app icon is stationary.

**Leverage varying opacity levels to increase the sense of depth and liveliness.** Creative use of opacity can make your icon stand out. For example, the Photos icon separates its centerpiece into multiple layers that contain translucent pieces, bringing greater liveliness to the design.

**Make sure your Home Screen icon adheres to safe-zone specifications.** During focus and parallax, the system may crop content around the edges of your app icon as the icon scales and moves. To ensure your icon’s content isn’t cropped too tightly, allow some additional space as shown in [tvOS app icon sizes](/design/human-interface-guidelines/app-icons#tvOS-app-icon-sizes)
.

### [visionOS](/design/human-interface-guidelines/app-icons#visionOS)

A visionOS app icon is circular and includes a background layer and one or two layers on top, producing a three-dimensional object that subtly expands when people view it.

![A blue square representing the background of the Safari app icon in visionOS.](https://docs-assets.developer.apple.com/published/0f54a2f61dd4d0834fd5a7976f72cc14/visionos-safari-icon-layer-background@2x.png)Background![A circular set of marks that represent the compass points layer of the Safari app icon in visionOS.](https://docs-assets.developer.apple.com/published/01d246c3a8d6407364c359093a52b637/visionos-safari-icon-layer-foreground-1@2x.png)Layer 1![An illustration representing the compass needle of the Safari app icon in visionOS.](https://docs-assets.developer.apple.com/published/1592dcd72ced39bd6cc1779414b2057c/visionos-safari-icon-layer-foreground-2@2x.png)Layer 2 [Play](#) 
The system enhances an app icon’s visual dimensionality by adding shadows to convey a sense of depth between layers and using the alpha channel of the upper layers to create an embossed appearance.

 [Play](#) 
**Use a full-bleed, non-transparent image for the background layer of your icon.** In contrast, avoid using full-bleed images in non-background layers. Using transparent areas in non-background layers lets visual information from underlying layers show through.

**Provide each layer as a square image.** The system uses a circular mask to crop all layers of an app icon and providing layers that are already cropped can negatively impact the result.

**Avoid using large areas of semi transparency.** Although using semi-transparent pixels to anti-alias a shape works fine, a large semi-transparent area doesn’t blend well with alpha and can combine with the system-provided shadow to produce a dark result. Unless you’re anti-aliasing a shape, keep pixels fully opaque or transparent.

![An illustration of an opaque circle that correctly represents the background layer of an app icon in visionOS.](https://docs-assets.developer.apple.com/published/9512342423cded42dd6cb7cbad463732/visionos-icon-layer-correct-example@2x.png)

![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration of a semi-transparent circle that incorrectly represents the background layer of an app icon in visionOS](https://docs-assets.developer.apple.com/published/7974cf6d2d9f66992a6b6cbdf351f3e7/visionos-icon-transparency-incorrect@2x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

**In non-background layers, prefer well-defined edges between distinct regions that are either fully opaque or transparent pixels.** The system-drawn highlights and shadows look best when non-background layers contain shapes that have clearly defined edges. Avoid using soft or feathered edges.

![An illustration of an opaque circle that correctly represents the background layer of an app icon in visionOS.](https://docs-assets.developer.apple.com/published/9512342423cded42dd6cb7cbad463732/visionos-icon-layer-correct-example@2x.png)

![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration of a circle with feathered, semi-transparent edges that incorrectly represents the background layer of an app icon in visionOS](https://docs-assets.developer.apple.com/published/601acf5be5480fb608138edd3403decc/visionos-icon-feathering-incorrect@2x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

**Avoid adding a shape that’s intended to look like a hole or concave area to the background layer.** The system-added shadow and specular highlights can make such a shape stand out instead of recede.

**Keep distinct shapes or images in non-background layers close to the center.** The circular mask can clip a shape or image when it’s too close to the edge, causing the shape to look off-center and spoiling the icon’s three-dimensional appearance.

**Avoid visual elements that give the appearance of depth from a fixed vantage point.** If people can perceive the depth of a layer’s inner element from only one perspective, this depth disappears when they bring focus to the icon. Avoid using a technique like extruding the bottom edge of a layer’s element, because doing so conflicts with the perpendicular perspective of other app icons.

**Avoid adding custom specular highlights or shadows to your visionOS app icon.** In addition to interfering with the system-provided visual effects, custom highlights and shadows are static whereas visionOS supplies dynamic ones.

For developer guidance, see [Configuring your app icon](/documentation/Xcode/configuring-your-app-icon)
.

### [watchOS](/design/human-interface-guidelines/app-icons#watchOS)

A watchOS app icon is circular and displays no accompanying text.

![An image of the Mail icon.](https://docs-assets.developer.apple.com/published/7c1ee3dcdce04cce614cfc19bf7d5cc8/icon-and-image-large-icon-mail@2x.png)

![An image of the Fitness icon.](https://docs-assets.developer.apple.com/published/321a6d197058a8d5d730d3f5883ef755/icon-and-image-large-icon-fitness@2x.png)

![An image of the Settings icon.](https://docs-assets.developer.apple.com/published/ebf3eff9f6a8b173b1601a16b809d5c5/icon-and-image-large-icon-settings@2x.png)

**Avoid using black for your icon’s background.** Lighten a black background or add a border so the icon doesn’t blend into the display background.

[Specifications](/design/human-interface-guidelines/app-icons#Specifications)
-----------------------------------------------------------------------------

### [App icon attributes](/design/human-interface-guidelines/app-icons#App-icon-attributes)

App icons in all platforms use the PNG format and support the following color spaces:

* sRGB (color)
* Gray Gamma 2.2 (grayscale)

In addition, app icons in iOS, iPadOS, macOS, tvOS, and watchOS support Display P3 (wide-gamut color).

The layers, transparency, and corner radius of an app icon can vary per platform. Specifically:



| Platform | Layers | Transparency | Asset shape |
| --- | --- | --- | --- |
| iOS, iPadOS | Single | No | Square |
| macOS | Single | Yes, as appropriate | Square with rounded corners |
| tvOS | Multiple | No | Rectangle |
| visionOS | Multiple | Yes, as appropriate | Square |
| watchOS | Single | No | Square |

### [App icon sizes](/design/human-interface-guidelines/app-icons#App-icon-sizes)

#### [iOS, iPadOS app icon sizes](/design/human-interface-guidelines/app-icons#iOS-iPadOS-app-icon-sizes)

You need to provide a large version of your app icon, measuring 1024x1024 pixels, to display in the App Store. You can let the system automatically scale down your large app icon to produce all other sizes, or — if you want to customize the appearance of the icon at specific sizes — you can supply multiple versions.



| @2x (pixels) | @3x (pixels) iPhone only | Usage |
| --- | --- | --- |
| 120x120 | 180x180 | Home Screen on iPhone |
| 167x167 | – | Home Screen on iPad Pro |
| 152x152 | – | Home Screen on iPad, iPad mini |
| 80x80 | 120x120 | Spotlight on iPhone, iPad Pro, iPad, iPad mini |
| 58x58 | 87x87 | Settings on iPhone, iPad Pro, iPad, iPad mini |
| 76x76 | 114x114 | Notifications on iPhone, iPad Pro, iPad, iPad mini |

#### [macOS app icon sizes](/design/human-interface-guidelines/app-icons#macOS-app-icon-sizes)

For the App Store, create a 1024x1024 px version of your macOS app icon. In addition, you also need to supply the icon in the following sizes.



| @1x (pixels) | @2x (pixels) |
| --- | --- |
| 512x512 | 1024x1024 |
| 256x256 | 512x512 |
| 128x128 | 256x256 |
| 32x32 | 64x64 |
| 16x16 | 32x32 |

#### [tvOS app icon sizes](/design/human-interface-guidelines/app-icons#tvOS-app-icon-sizes)

For the App Store, create a 1280x768 px version of your tvOS app icon. In addition, you also need to supply the icon in the following sizes.



| @1x (pixels) | @2x (pixels) | Usage |
| --- | --- | --- |
| 400x240 | 800x480 | Home Screen |

**Consider allowing a safe zone in your Home Screen icon.** During focus and parallax, content around the edges of your app icon may be cropped as the icon scales and moves. To ensure your icon’s content isn’t cropped too tightly, you might want to include some additional breathing room.

#### [visionOS app icon sizes](/design/human-interface-guidelines/app-icons#visionOS-app-icon-sizes)

Create an app icon that measures 1024x1024 px for display in the Home View.

#### [watchOS app icon sizes](/design/human-interface-guidelines/app-icons#watchOS-app-icon-sizes)

For the App Store, create a 1024x1024 px version of your watchOS app icon. You can let the system automatically scale this version down to all other sizes, or — if you want to customize the appearance of your app icon at specific sizes — you can supply the sizes listed in the following table. All icon dimensions are shown in pixels @2x.



| 38mm | 40mm | 41mm | 42mm | 44mm | 45mm | 49mm | Usage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 80x80 | 88x88 | 92x92 | 80x80 | 100x100 | 102x102 | 108x108 | Home Screen |
| 48x48 | 55x55 | 58x58 | 55x55 | 58x58 | 66x66 | 66x66 | Notification Center |
| 172x172 | 196x196 | 196x196 | 196x196 | 216x216 | 234x234 | 258x258 | Short look |

If you have a companion iPhone app, you also need to supply your watchOS app icon in the following sizes.



| @2x (pixels) | @3x (pixels) |
| --- | --- |
| 58x58 | 87x87 |

[Resources](/design/human-interface-guidelines/app-icons#Resources)
-------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/app-icons#Related)

[Apple Design Resources](https://developer.apple.com/design/resources/)


#### [Developer documentation](/design/human-interface-guidelines/app-icons#Developer-documentation)

[Configuring your app icon](/documentation/Xcode/configuring-your-app-icon)


#### [Videos](/design/human-interface-guidelines/app-icons#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/7/74B6B85B-5D99-48E7-B103-BE1514D8A4DA/1913_wide_250x141_1x.jpg) App Icon Design](https://developer.apple.com/videos/play/wwdc2017/822) 
[Change log](/design/human-interface-guidelines/app-icons#Change-log)
---------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Added specifications for Apple Watch Ultra. |

