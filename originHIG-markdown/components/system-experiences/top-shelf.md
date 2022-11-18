# **[components-status] top-shelf**

## The Apple TV Home Screen provides an area called Top Shelf, which showcases your content in a rich, engaging way while also giving people access to their favorite apps in the Dock.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/top-shelf-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/top-shelf-intro-dark_2x.png)

When you support full-screen Top Shelf, people can swipe through multiple full-screen content views, play trailers and previews, and get more information about your content.

Top Shelf is a unique opportunity to highlight new, featured, or recommended content and let people jump directly to your app or game to view it. For example, when people select Apple TV in the Dock, full-screen previews immediately begin playing and soon the Dock slides away. As people watch previews for the first show, they can swipe through previews of all other featured shows, stopping to select Play or More Info for a preview that interests them.

The system defines several layout templates that you can use to give people a compelling Top Shelf experience when they select your app in the Dock. To help you position content, you can download these templates from [Apple Design Resources](https://developer.apple.com/design/resources/#tvos-apps).

# **Best practices**

**Help people jump right into your content.** Top Shelf provides a path to the content people care about most. Two of the system-provided layout templates — [carousel actions](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf#carousel-actions) and [carousel details](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf#carousel-details) — each include two buttons by default: A primary button intended to begin playback and a More Info button intended to open your app to a view that displays details about the content.

**Feature new content.** For example, showcase new releases or episodes, highlight upcoming movies and shows, and avoid promoting content that people have already purchased, rented, or watched.

**Personalize people’s favorite content.** People typically put the apps they use most often into Top Shelf. You can personalize their experience by showing targeted recommendations in the Top Shelf content you supply, letting people resume media playback or jump back into active gameplay.

**Avoid showing advertisements or prices.** People put your app into Top Shelf because you’ve already sold them on it, so they may not appreciate seeing lots of ads from your app. Showing purchasable content in the Top Shelf is fine, but prefer putting the focus on new and exciting content, and consider displaying prices only when people show interest.

**Showcase compelling dynamic content.** The videos and images you show in the Top Shelf should draw people in and encourage them to view more. If necessary, you can supply static images, but people typically prefer a captivating, dynamic Top Shelf experience that features the newest or highest rated content. To provide this experience, prefer creating [layered images](https://developer.apple.com/design/human-interface-guidelines/foundations/images/#layered-images) to display in Top Shelf.

**If you don't provide the recommended full-screen content, supply at least one static image as a fallback.** The system displays a static image when your app is in the Dock and in focus and full-screen content is unavailable. tvOS flips and blurs the image, ensuring that it fits into a width of 1920 pixels at the 16:9 aspect ratio. Use the following values for guidance.

| Image size (@1x) | Image size (@2x) |
| --- | --- |
| 2320px × 720px (2320pt × 720pt @1x) | 4640px × 1440px (2320pt × 720pt @2x) |

**Avoid implying interactivity in a static image.** A static Top Shelf image isn’t focusable, and you don’t want to make people think it’s interactive.

# **Dynamic layouts**

Dynamic Top Shelf imagery can appear in several ways:

- A carousel of full-screen video and images that includes two buttons and optional details
- A row of focusable content
- A set of scrolling banners

# **Carousel actions**

The carousel actions layout style focuses on full-screen video and images and includes a few unobtrusive controls that help people see more. This layout style works especially well to showcase content that people already know something about. For example, it's great for displaying user-generated content, like photos, or new content from a franchise or show that people are likely to enjoy.

**Provide a title.** Include a succinct title, like the title of the show or movie or the title of a photo album. If necessary, you can also provide a brief subtitle. For example, a subtitle for a photo album could be a range of dates; a subtitle for an episode could be the name of the show.

# **Carousel details**

This layout style extends the carousel actions layout style, giving you the opportunity to include some information about the content. For example, you might provide information like a plot summary, cast list, and other metadata that helps people decide whether to choose the content.

**Provide a title that identifies the currently playing content.** The content title appears near the top of the screen so it's easy for people to read it at a glance. Above the title, you can also provide a succinct phrase or app attribution, like "Featured on *My App*."

# **Sectioned content row**

This layout style shows a single labeled row of sectioned content, which can work well to highlight recently viewed content, new content, or favorites. Row content is focusable, which lets people scroll quickly through it. A label appears when an individual piece of content comes into focus, and small movements on the remote’s Touch surface bring the focused image to life. You can also configure a sectioned content row to show multiple labels.

**Provide enough content to constitute a complete row.** At a minimum, load enough images in a sectioned content row to span the full width of the screen. In addition, include at least one label for greater platform consistency and to provide additional context.

You can use the following image sizes in a sectioned content row.

### **Poster (2:3)**

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-2x3-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-2x3-dark_2x.png)

| Aspect | Image size (@1x) | Image size (@2x) |
| --- | --- | --- |
| Actual size | 404px × 608px (404pt × 608pt @1x) | 808px × 1216px (404pt × 608pt @2x) |
| Focused/Safe zone size | 380px × 570px (380pt × 570pt @1x) | 760px × 1140px (380pt × 570pt @2x) |
| Unfocused size | 333px × 570px (333pt × 570pt @1x) | 666px × 1140px (333pt × 570pt @2x) |

### **Square (1:1)**

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-1x1-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-1x1-dark_2x.png)

| Aspect | Image size (@1x) | Image size (@2x) |
| --- | --- | --- |
| Actual size | 608px × 608px (608pt × 608pt @1x) | 1216px × 1216px (608pt × 608pt @2x) |
| Focused/Safe zone size | 570px × 570px (570pt × 570pt @1x) | 1140px × 1140px (570pt × 570pt @2x) |
| Unfocused size | 500px × 500px (500pt × 500pt @1x) | 1000px × 1000px (500pt × 500pt @2x) |

### **16:9**

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-16x9-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-16x9-dark_2x.png)

| Aspect | Image size (@1x) | Image size (@2x) |
| --- | --- | --- |
| Actual size | 908px × 512px (908pt × 512pt @1x) | 1816px × 1024px (908pt × 512pt @2x) |
| Focused/Safe zone size | 852px × 479px (852pt × 479pt @1x) | 1704px × 958px (852pt × 479pt @2x) |
| Unfocused size | 782px × 440px (782pt × 440pt @1x) | 1564px × 880px (782pt × 440pt @2x) |

**Be aware of additional scaling when combining image sizes.** If your Top Shelf design includes a mixture of image sizes, keep in mind that images will automatically scale up to match the height of the tallest image if necessary. For example, a 16:9 image scales to 500 pixels high if included in a row with a poster or square image.

### **Scrolling inset banner**

This layout shows a series of large images, each of which spans almost the entire width of the screen. Apple TV automatically scrolls through these banners on a preset timer until people bring one into focus. The sequence circles back to the beginning after the final image is reached.

When a banner is in focus, a small, circular gesture on the remote’s Touch surface enacts the system focus effect, animating the item, applying lighting effects, and, if the banner contains layered images, producing a 3D effect. Swiping on the Touch surface pans to the next or previous banner in the sequence. Use this style to showcase rich, captivating content, such as a popular new movie.

**Provide three to eight images.** A minimum of three images is recommended for a scrolling banner to feel effective. More than eight images can make it hard to navigate to a specific image.

**If you need text, add it to your image.** This layout style doesn’t show labels under content, so all text must be part of the image itself. In layered images, consider elevating text by placing it on a dedicated layer above the others. Add the text to the accessibility label of the image too, so [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility#voiceover)can read it.

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-extra-wide_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-extra-wide_2x.png)

Use the following size for a scrolling inset banner image:

| Aspect | Image size (@1x) | Image size (@2x) |
| --- | --- | --- |
| Actual size | 1940px × 692px (1940pt × 692pt @1x) | 3880px × 1384px (1940pt × 692pt @2x) |
| Focused/Safe zone size | 1740px × 620px (1740pt × 620pt @1x) | 3480px × 1240px (1740pt × 620pt @2x) |
| Unfocused size | 1740px × 560px (1740pt × 560pt @1x) | 3480px × 1120px (1740pt × 560pt @2x) |