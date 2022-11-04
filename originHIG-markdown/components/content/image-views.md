# **[content] image-views**

## An image view displays a single image — or in some cases, an animated sequence of images — on a transparent or opaque background.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/image-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/image-view-intro-dark_2x.png)

Within an image view, you can stretch, scale, size to fit, or pin the image to a specific location. Image views are typically not interactive.

# **Best practices**

**Use an image view when the primary purpose of the view is simply to display an image.** In rare cases where you might want an image to be interactive, configure a system-provided [button](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons) to display the image instead of adding button behaviors to an image view.

**If you want to display an icon in your interface, consider using a symbol or interface icon instead of an image view.** [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols) provides a large library of streamlined, vector-based images that you can render with various colors and opacities. An [interface icon](https://developer.apple.com/design/human-interface-guidelines/foundations/icons) (also called a glyph or template image) is typically a bitmap image in which the nontransparent pixels can receive color. Both symbols and interface icons can use the accent colors people choose.

# **Content**

An image view can contain rich image data in various formats, like PNG, JPEG, and PDF. For more guidance, see [Images](https://developer.apple.com/design/human-interface-guidelines/foundations/images).

**Take care when overlaying text on images.** Compositing text on top of images can decrease both the clarity of the image and the legibility of the text. To help improve the results, ensure the text contrasts well with the image, and consider ways to make the text object stand out, like adding a text shadow or background layer.

**Aim to use a consistent size for all images in an animated sequence.**When you prescale images to fit the view, the system doesn't have to perform any scaling. In cases where the system must do the scaling, performance is generally better when all images are the same size and shape.

# **Platform considerations**

*No additional considerations for iOS or iPadOS.*

# **macOS**

**If your app needs an editable image view, use an image well.** An [image well](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/image-wells) is an image view that supports copying, pasting, dragging, and using the Delete key to clear its content.

**Use an image button instead of an image view to make a clickable image.** An [image button](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/#image-buttons) contains an image or icon, appears in a view, and initiates an instantaneous app-specific action.

# **tvOS**

Many tvOS images combine multiple layers with transparency to create a feeling of depth. For guidance, see [Layered Images](https://developer.apple.com/design/human-interface-guidelines/foundations/images/#layered-images).

# **watchOS**

**Use SwiftUI to create animations when possible.** If necessary, you can use WatchKit to animate a sequence of images within an image element. For developer guidance, see [WKImageAnimatable](https://developer.apple.com/documentation/watchkit/wkimageanimatable).