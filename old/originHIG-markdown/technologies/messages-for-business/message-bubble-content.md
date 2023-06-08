# **[technologies-messages-for-business] message-bubble-content**

Message bubbles for standard interactive messages like Apple Pay payment requests, rich links, and pickers include a title, and can optionally include additional text and an image (which can be a video thumbnail). Optional text includes a primary, secondary, and tertiary subtitle, and an image title and subtitle.

# **Message bubble layout styles**

Message bubbles for standard interactive messages support the following layout styles.

| Style | Description | Size |
| --- | --- | --- |
| Icon | Horizontal bubble with an icon | 280x65 pt |
| Small | Horizontal bubble with a small image | 280x85 pt |
| Large | Horizontal bubble with a large image | 280x210 pt |

**Scale images based on the layout style.** When using the same image for multiple layout styles, provide a scaled image variation for each layout style. See [Image sizes](https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/message-bubble-content#image-sizes) for sizing guidance.

# **Images for message bubbles**

In a conversation, you can add an image to an interactive message bubble to provide greater context. When asking the customer to choose a product, for example, you could show product photos in a list picker to help people visually distinguish the items. Or, when requesting payment, you could show the item being purchased in the Apple Pay message bubble.

When you include a rich link to a video in a message bubble, you supply a thumbnail image that represents the video. The following size and resolution guidelines apply equally to images and video thumbnails.

### **Image sizes**

Provide images at the following sizes, based on where the images are used. When displaying the same image at multiple sizes, provide a separate image for each size.

| Usage | Image Size |
| --- | --- |
| Interactive message message bubble (icon) | 40x40 pt (120x120 px @3x) |
| Interactive message message bubble (small) | 60x60 pt (180x180 px @3x) |
| Interactive message message bubble (large) | 263x150 pt (789x450 px @3x) |
| List picker image | 60x60 pt (180x180 px @3x) |

### **Designing high-resolution images**

A standard-resolution display has a 1:1 pixel density (or @1x), where one pixel is equal to one point. High-resolution displays have a higher pixel density, offering a scale factor of 2.0 or 3.0 (referred to as @2x and @3x). As a result, high-resolution displays demand images with more pixels.

![https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/ImageResolution-Graphic_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/ImageResolution-Graphic_2x.png)

For example, suppose you have a standard resolution (@1x) image that’s 100x100 px. The @2x version of this image would be 200x200 px, and the @3x version would be 300x300 px.

**Always provide high-resolution images with a scale factor of @3x.** The @3x images you provide automatically scale down to @2x or @1x for display at lower resolutions.

**Produce artwork in the appropriate format.** Use de-interlaced PNG files for bitmap/raster artwork. Use JPEG for photos.

**Use the 8-bit color palette for PNG graphics that don’t require full 24-bit color.** Using an 8-bit color palette reduces file size without reducing image quality.

**Optimize JPEG files to find a balance between size and quality.** Most JPEG files can be compressed without noticeable degradation of the resulting image. Even a small amount of compression can save significant disk space. Experiment with compression settings on each image to find the optimal value that yields an acceptable result.