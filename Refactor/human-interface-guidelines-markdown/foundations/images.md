Updated to include guidance for visionOS. Images
======

To make sure your artwork looks great on all devices you support, learn how the system displays content and how to deliver art at the appropriate scale factors.![A sketch of a photo, suggesting imagery. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/b0a68ac859ddb098858e92609997d307/foundations-images-intro@2x.png)

[Resolution](/design/human-interface-guidelines/images#Resolution)
------------------------------------------------------------------

Different devices can display images at different resolutions. For example, a 2D device displays images according to the resolution of its screen.

A *point* is an abstract unit of measurement that helps visual content remain consistent regardless of how it’s displayed. In 2D platforms, a point maps to a number of pixels that can vary according to the resolution of the display; in visionOS, a point is an angular value that allows visual content to scale according to its distance from the viewer.

To identify the resolution of an image you create, you specify a *scale factor*. You can visualize scale factor by considering the density of pixels per point in 2D displays of various resolutions. For example, a scale factor of 1 (also called @1x) describes a 1:1 pixel density, where one pixel is equal to one point. High-resolution 2D displays have higher pixel densities, such as 2:1 or 3:1. A 2:1 density (called @2x) has a scale factor of 2, and a 3:1 density (called @3x) has a scale factor of 3. Because of higher pixel densities, high-resolution displays demand images with more pixels.

![Image of a circle that is in standard resolution at scale factor 1 and has 10 x 10 pixels.](https://docs-assets.developer.apple.com/published/a9b04545f30aff45ca503e263c02d464/image-resolution-1x@2x.png)1x (10x10 px)![Image of a circle that is in high resolution at scale factor 2 and has 20 x 20 pixels.](https://docs-assets.developer.apple.com/published/cf203acc0ee6299833fb2e5b5c4a7348/image-resolution-2x@2x.png)2x (20x20 px)![Image of a circle that is in high resolution at scale factor 3 and has 30 x 30 pixels.](https://docs-assets.developer.apple.com/published/0de9ee5144fc2278682eb211ac8f571d/image-resolution-3x@2x.png)3x (30x30 px)[Formats](/design/human-interface-guidelines/images#Formats)
------------------------------------------------------------

As you create different types of images, consider the following recommendations.



| Image type | Format |
| --- | --- |
| Bitmap or raster work | De-interlaced PNG files |
| PNG graphics that don’t require full 24-bit color | An 8-bit color palette |
| Photos | JPEG files, optimized as necessary, or HEIC files |
| Flat icons, interface icons, and other flat artwork that requires high-resolution scaling | PDF or SVG files |

[Best practices](/design/human-interface-guidelines/images#Best-practices)
--------------------------------------------------------------------------

**Supply high-resolution images for all artwork in your app, for every device you support.** As you add each image to your project’s asset catalog, identify its scale factor by appending “@1x,” “@2x,” or “@3x” to its filename. Use the following values for guidance; for additional scale factors, see [Layout](/design/human-interface-guidelines/layout)
.



| Platform | Scale factors |
| --- | --- |
| iPadOS, visionOS, watchOS | @2x |
| iOS | @2x and @3x |
| macOS, tvOS | @1x and @2x |

**In general, design images at the lowest resolution and scale them up to create high-resolution assets.** When you use resizable vectorized shapes, you might want to position control points at whole values so that they’re cleanly aligned at 1x. This positioning allows the points to remain cleanly aligned to the raster grid at higher resolutions, because 2x and 3x are multiples of 1x. In contrast, there are times when you don’t want to keep a shape perfectly aligned to the raster grid; for example, aligning a circle to the grid can make it appear flattened at the top and bottom.

**Include a color profile with each image.** Color profiles help ensure that your app’s colors appear as intended on different displays. For guidance, see [Color management](/design/human-interface-guidelines/color#Color-management)
.

**Always test images on a range of actual devices.** An image that looks great at design time may appear pixelated, stretched, or compressed when viewed on various devices.

[Platform considerations](/design/human-interface-guidelines/images#Platform-considerations)
--------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, or macOS.*

### [tvOS](/design/human-interface-guidelines/images#tvOS)

Layered images are at the heart of the Apple TV user experience. The system combines layered images, transparency, scaling, and motion to produce a sense of realism and vigor that evokes a personal connection as people interact with onscreen content.

#### [Parallax effect](/design/human-interface-guidelines/images#Parallax-effect)

*Parallax* is a subtle visual effect the system uses to convey depth and dynamism when an element is in focus. As an element comes into focus, the system elevates it to the foreground, gently swaying it while applying illumination that makes the element’s surface appear to shine. After a period of inactivity, out-of-focus content dims and the focused element expands.

Layered images are required to support the parallax effect.

#### [Layered images](/design/human-interface-guidelines/images#Layered-images)

A *layered image* consists of two to five distinct layers that come together to form a single image. The separation between layers, along with use of transparency, creates a feeling of depth. As someone interacts with an image, layers closer to the surface elevate and scale, overlapping lower layers farther back and producing a 3D effect.

Important

Your tvOS [app icon](https://developer.apple.com/design/human-interface-guidelines/app-icons)
 must use a layered image. For other focusable images in your app, including [Top Shelf](/design/human-interface-guidelines/top-shelf)
 images, layered images are strongly encouraged, but optional.

**Use standard interface elements to display layered images.** If you use standard views and system-provided focus APIs — such as [`FocusState`](/documentation/SwiftUI/FocusState)
 — layered images automatically get the parallax treatment when people bring them into focus.

**Identify logical foreground, middle, and background elements.** In foreground layers, display prominent elements like a character in a game, or text on an album cover or movie poster. Middle layers are perfect for secondary content and effects like shadows. Background layers are opaque backdrops that showcase the foreground and middle layers without upstaging them.

**Generally, keep text in the foreground.** Unless you want to obscure text, bring it to the foreground layer for clarity.

**Keep the background layer opaque.** Using varying levels of opacity to let content shine through higher layers is fine, but your background layer must be opaque — you’ll get an error if it’s not. An opaque background layer ensures your artwork looks great with parallax, drop shadows, and system backgrounds.

**Keep layering simple and subtle.** Parallax is designed to be almost unnoticeable. Excessive 3D effects can appear unrealistic and jarring. Keep depth simple to bring your content to life and add delight.

**Leave a safe zone around your content.** During focus and parallax, content around the edges of some layers may be cropped or difficult to see clearly as the image scales and moves. To ensure that your primary content is always visible, don’t put it too close to the edges. Be aware that the safe zone can vary, depending on the image size, layer depth, and motion, and that foreground layers are cropped more than background layers.

![Image of an icon with a dotted line inside the outer border, which indicates the safe zone.](https://docs-assets.developer.apple.com/published/941fcf33660f94464f60403ad7b3dd17/icons-and-images-icon-safe-zone@2x.png)

**Always preview layered images.** To ensure your layered images look great on Apple TV, preview them throughout your design process using Xcode, the Parallax Previewer app for macOS, or the Parallax Exporter plug-in for Adobe Photoshop. Pay special attention as scaling and clipping occur, and readjust your images as needed to keep important content safe. After your layered images are final, preview them on an actual TV for the most accurate representation of what people will see. To download Parallax Previewer and Parallax Exporter, see [Resources](https://developer.apple.com/design/resources/#tvos-apps)
.

**Use both the unfocused and focused states to determine the appropriate size for a layered image.** During the parallax effect, the system may crop background layers slightly, so keep essential content within a safe zone and include some additional space to make sure your content looks good.

![Diagram of a layered image, which shows the outermost, actual size, the inner focused or safe zone size, and the innermost unfocused size. The diagram also shows the 35 point side margins between the unfocused and focused areas.](https://docs-assets.developer.apple.com/published/51bbe8a18e9f50356087bd7b8d9692a4/layered-image-zones@2x.png)

The following formulas can help you calculate sizing for a layered image based on the size of the image when it’s not in focus.



| Image side | Focused/Safe zone size | Actual size |
| --- | --- | --- |
| Longest | Length of longest unfocused side + 70 pt | Length of longest focused side x 106% |
| Shortest | Proportional based on longest side | Proportional based on longest side |

You can embed layered images in your app or retrieve them from a content server at runtime. To create layered images for inclusion within your app, use one of the following tools:

* **Parallax Previewer app for macOS.** Parallax Previewer can import PNG files to serve as individual layers, layered images (`.lsr`) created with the Parallax Exporter plug-in, and layered Photoshop images (`.psd`). Parallax Previewer can export LSR files that you can import directly into an Xcode project.
* **Parallax Exporter Adobe Photoshop plug-in.** Use this plug-in to test your layered images in Photoshop and export them as LSR files that you can import directly into an Xcode project.
* **Xcode.** Drag standard PNG files into your app’s asset catalog to serve as individual layers of an image stack in Xcode. Image stacks can be exported as LSR files. Xcode can also import LSR files.

If your app retrieves layered images from a content server at runtime, you must provide those images in runtime layered image (`.lcr`) format. You don’t create runtime layered images directly; you generate them from LSR files or Photoshop files using the `layerutil` command-line tool that Xcode provides. Runtime layered images are intended to be downloaded — don’t embed them within your app.

### [visionOS](/design/human-interface-guidelines/images#visionOS)

In visionOS, the area an image occupies typically varies when the system dynamically scales it according to the distance and angle at which people view it. This means that an image doesn’t line up 1:1 with screen pixels as it can in other platforms.

**Create a multilayered image for your visionOS app icon.** For guidance, see [App icons](/design/human-interface-guidelines/app-icons)
.

**Prefer vector-based art.** Avoid bitmap content because it might not look good when the system scales it up. If you use Core Animation layers, see [Drawing sharp layer-based content in visionOS](/documentation/visionOS/drawing-sharp-layer-based-content)
 for developer guidance.

**Create @2x images.** Using a high resolution helps ensure that an image appears sharp when the system scales it. For guidance, see [Scale](/design/human-interface-guidelines/spatial-layout#Scale)
.

### [watchOS](/design/human-interface-guidelines/images#watchOS)

**In general, avoid transparency to keep image files small.** If you always composite an image on the same solid background color, it’s more efficient to include the background in the image. However, transparency is necessary in complication images, menu icons, and other interface icons that serve as template images, because the system uses it to determine where to apply color.

**Use autoscaling PDFs to let you provide a single asset for all screen sizes.** Design your image for the 40mm and 42mm screens at 2x. When you load the PDF, WatchKit automatically scales the image based on the device’s screen size, using the values shown below:



| Screen size | Image scale |
| --- | --- |
| 38mm | 90% |
| 40mm | 100% |
| 41mm | 106% |
| 42mm | 100% |
| 44mm | 110% |
| 45mm | 119% |
| 49mm | 119% |

[Resources](/design/human-interface-guidelines/images#Resources)
----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/images#Related)

[Apple Design Resources](https://developer.apple.com/design/resources/)


#### [Developer documentation](/design/human-interface-guidelines/images#Developer-documentation)

[Drawing sharp layer-based content in visionOS](/documentation/visionOS/drawing-sharp-layer-based-content)


[`UIImageView`](/documentation/uikit/uiimageview)


[`NSImageView`](/documentation/appkit/nsimageview)


[`FocusState`](/documentation/SwiftUI/FocusState)


#### [Videos](/design/human-interface-guidelines/images#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/7/09438FDD-3E8B-42A3-A364-78E1A7F2CE6B/1915_wide_250x141_1x.jpg) Get Started with Display P3](https://developer.apple.com/videos/play/wwdc2017/821) 
[Change log](/design/human-interface-guidelines/images#Change-log)
------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Added specifications for Apple Watch Ultra. |

