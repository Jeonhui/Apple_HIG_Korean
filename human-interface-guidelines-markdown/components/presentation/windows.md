June 21, 2023

 Updated to include guidance for visionOS. Windows
=======

A window contains the views and components that present the user interface of your app or game.![A stylized representation of a window with close, minimize, and full-screen buttons. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/e678408ee6b4eb19f2cfed9a9e4cef47/components-window-intro@2x.png)

Depending on the platform, device, and context, a window (or *scene*) can be undetectable to people. For example, in platforms where the default experience is full screen, like iOS, tvOS, and watchOS, people view and interact with the content inside a window — they don’t view or interact with the window itself. In these cases, you don’t need to design the appearance of the window or scene itself in your app or game. For developer guidance, see [`Scene`](/documentation/SwiftUI/Scene)
 and [`UIWindow`](/documentation/uikit/uiwindow)
.

Note

In SwiftUI, a scene is a part of an app’s interface that can contain windows and view hierarchies. The terms *window* and *scene* are often used synonymously, especially in design guidance, but in help and other content that describes your app to people, use *window* — not *scene* — if you need to refer to these high-level content containers.

In [visionOS](/design/human-interface-guidelines/windows#visionOS)
, [iPadOS](/design/human-interface-guidelines/windows#iPadOS)
, and [macOS](/design/human-interface-guidelines/windows#macOS)
 — in contrast to iOS, tvOS, and watchOS — people are aware of windows as visually distinct objects, because they can typically open, close, resize, and relocate individual windows, as well as view multiple windows at the same time. In visionOS, people can also interact with a *volume*, which is a container optimized for displaying 3D content that people can view from any angle; for guidance, see [Volumes](/design/human-interface-guidelines/windows#Volumes)
.

The guidance below applies to windows that people can view and manipulate as separate objects. For guidance on other types of window-like views in all platforms, see [Alerts](/design/human-interface-guidelines/alerts)
, [Panels](/design/human-interface-guidelines/panels)
, [Popovers](/design/human-interface-guidelines/popovers)
, and [Sheets](/design/human-interface-guidelines/sheets)
.

For guidance laying out content within a window or scene, see [Layout](/design/human-interface-guidelines/layout)
; for guidance laying out content in Apple Vision Pro space, see [Spatial layout](/design/human-interface-guidelines/spatial-layout)
.

[Platform considerations](/design/human-interface-guidelines/windows#Platform-considerations)
---------------------------------------------------------------------------------------------

*No additional considerations for iOS, tvOS, or watchOS.*

### [iPadOS](/design/human-interface-guidelines/windows#iPadOS)

In iPadOS, multitasking and multiple windows features mean that people can be aware of an app’s window as a visually distinct object. For example, people can view two or three apps onscreen at the same time or open multiple windows in the same app. To create a great iPadOS experience, you need to ensure that your windows and scenes look and behave the way people expect. For developer guidance, see [`Scene`](/documentation/SwiftUI/Scene)
.

To support multitasking and multiwindow workflows on iPad, you need to ensure that your windows adapt to different sizes and that you match each window’s presentation style to its content. For guidance, see [Multitasking on iPad](/design/human-interface-guidelines/multitasking#Multitasking-on-iPad)
.

### [macOS](/design/human-interface-guidelines/windows#macOS)

Mac users typically run several apps at the same time, often viewing windows from multiple apps on one desktop and switching frequently between different windows — moving, resizing, minimizing, and revealing the windows to suit their work style. Even when people choose [full-screen mode](/design/human-interface-guidelines/going-full-screen)
, which usually hides the window frame, the built-in, full-screen transition and the ability to reveal the toolbar remind them of the existence of the window.

#### [macOS window anatomy](/design/human-interface-guidelines/windows#macOS-window-anatomy)

A macOS window consists of a frame and a body area. People can move a window by dragging the frame and can often resize the window by dragging its edges.

![An illustration that represents a Finder window in macOS, with callouts indicating the window frame area at the top and the body area below it.](https://docs-assets.developer.apple.com/published/cab49db40aadf8c61c8ba7081851d721/window-anatomy@2x.png)

The *frame* is the portion of a window that surrounds body content. A window frame can include a title bar, [toolbar](/design/human-interface-guidelines/toolbars)
, [tabs](/design/human-interface-guidelines/tab-views)
, and (in rare cases) a bottom bar.

The window *body* displays the main content of the window. This content can fill the entire body area — such as a website in a Safari window or an image in Preview — or the content can display in multiple subviews, such as in a [split view](/design/human-interface-guidelines/split-views)
 interface. Content that extends beyond the bounds of views in the body area is scrollable.

#### [macOS window states](/design/human-interface-guidelines/windows#macOS-window-states)

A macOS window can have one of three states:

* **Main.** The frontmost window that people focus on is an app’s main window. There can be only one main window per app.
* **Key.** Also called the active window, the key window accepts people’s input. There can be only one key window onscreen at a time. Although the front app’s main window is usually the key window, another window — such as a panel floating above the main window — might be key instead. People typically click a window to make it key; when people click an app’s Dock icon to bring all of that app’s windows forward, only the most recently accessed window becomes key.
* **Inactive.** A window that’s not in the foreground is an inactive window.

The system gives main, key, and inactive windows different appearances to help people visually identify them. For example, the key window uses color in the title bar options for closing, minimizing, and zooming; inactive windows and main windows that aren’t key use gray in these options. Also, inactive windows don’t use [vibrancy](/design/human-interface-guidelines/materials)
 (an effect that can pull color into a window from the content underneath it), which makes them appear subdued and seem visually farther away than the main and key windows.

![A stack of three windows, as follows: An inactive window in the background, an app’s main window in the middle, and a key window appearing above the other two windows.](https://docs-assets.developer.apple.com/published/81d1c6ada94f4ff7f9309d56358a4d4b/window-states@2x.png)

Note

Some windows — typically, panels like Colors or Fonts — become the key window only when people click the window’s title bar or a component that requires keyboard input, such as a text field.

#### [Using windows in a macOS app](/design/human-interface-guidelines/windows#Using-windows-in-a-macOS-app)

**Make sure your custom windows use the system-defined appearances.** People rely on the visual differences in various onscreen windows to help them identify the foreground window and know which window will accept their input. When you use system-provided components, a window’s background and button appearances update automatically when the window changes state; if you use custom implementations, you need to do this work yourself.

**Display a title unless the window’s content provides enough context to make one unnecessary.** For document windows, the title is the name of the document or *Untitled* (for new documents). For app windows, the title is the name of the app.

**If you need to use a filename as a title, make it easy to understand.** For example, use the file’s *display name,* which reflects people’s preference for showing or hiding a file extension and may be localized.

**Avoid including a file system path in the title bar.** Paths are generally too long to fit in the title bar without clipping, and they’re difficult for people to understand at a glance. If you need to show the complete path of a file or folder, do so in another way, like in an inspector pane.

**Use numeric suffixes to differentiate duplicate titles.** The first instance of a title doesn’t need a numeric suffix. When other windows have the same title, append numeric suffixes, starting with *2*. For example, *Untitled*, *Untitled 2*, *Untitled 3*.

**Make sure people can still interact with your window if you hide the title bar.** Provide alternative ways — like menus — to close and minimize the window. Make sure people can still drag the frame to move the window. If the window has a toolbar and no title bar, make sure there’s enough space in the toolbar to drag the window without activating toolbar items.

**In general, use a dot to mark a modified document as unsaved only when it can’t be autosaved.** If a document can be autosaved, you don’t want to display a dot in the window’s close button or next to the document’s name in the Window menu because doing so signals that people need to take action to save their changes. It’s fine to append a suffix like *Edited* to the document’s title in the title bar, but you need to remove this suffix when it autosaves or if people manually perform a save.

**Use a bottom bar to display a small amount of information directly related to a window’s contents or to a selected item within it.** For example, Finder uses a bottom bar (called the Status Bar) to display the total number of items in a window, the number of selected items, and how much space is available on the disk. A bottom bar is small, so if you have more information to display, consider using an inspector, which typically presents information on the trailing side of a split view.

**Avoid putting critical information or actions in a bottom bar.** People often relocate a window in a way that hides its bottom edge.

### [visionOS](/design/human-interface-guidelines/windows#visionOS)

A visionOS app can use windows or volumes to display content in a container. In general, you use a window to present 2D or 3D content, like the Inbox in Mail or a webpage in Safari that contains a USDZ object. To present 3D content and objects — like a game board or a globe — you typically use a [volume](/design/human-interface-guidelines/windows#Volumes)
.

![An illustration representing a window in visionOS. The illustration consists of two parallel rounded rectangles, slightly separated and displayed on an angle, positioned above a window bar.](https://docs-assets.developer.apple.com/published/e8dc51484c2e5f3289a5f6a878f4c47d/visionos-window-style-2d-window@2x.png)A window![An illustration representing a volume in visionOS. The illustration consists of a translucent cube. The base of the cube is darker than the other sides. The front of the cube is positioned above a window bar.](https://docs-assets.developer.apple.com/published/92d953d099f72f9909c47bad408f4c9b/visionos-window-style-3d-volume@2x.png)A volumeNote

The system defines the initial position of each window and volume people open. In both the *Shared Space* and a *Full Space*, people can move windows and volumes to new locations.

People are instantly familiar with windows in visionOS because they look and behave similarly to the distinct windows in other platforms. For example, a visionOS window aligns with an upright plane, can appear alongside other app windows in the Shared Space, and provides system-defined controls that let people move, resize, and close it. In addition to window-management controls, a window can also include a share menu, [tab bar](/design/human-interface-guidelines/tab-bars)
, [toolbar](/design/human-interface-guidelines/toolbars)
, and one or more [ornaments](/design/human-interface-guidelines/ornaments)
.

![A screenshot of a window for an app named 'Hello World' in visionOS. The window includes text and buttons for entering different experiences.](https://docs-assets.developer.apple.com/published/80faa14372917ec4745df9e894e9bc90/visionos-window-2d@2x.png)A windowA visionOS window uses an unmodifiable background [material](/design/human-interface-guidelines/materials)
 called *glass*, which lets light and both physical and virtual objects show through. A glass window helps your content feel like part of people’s surroundings while using specular reflections and shadows to communicate the window’s scale and position. When you create a window using the default style, you automatically get the glass background. For developer guidance, see [`DefaultWindowStyle`](/documentation/SwiftUI/DefaultWindowStyle)
.

By default, a window measures 1306 x 734 pt. When a window first opens, the system places it about two meters in front of the wearer, giving it an apparent width of about three meters.

The system also adds highlights and shadows to the views and controls within a standard window, giving them the appearance of [depth](/design/human-interface-guidelines/spatial-layout#Depth)
 and helping them feel more substantial, especially when people view the window from an angle. Although you can display 3D content in a standard window, the system clips it if the content extends too far from the window’s surface. To display 3D content that has greater depth, use a volume.

![A screenshot of a window for an app in visionOS. The window includes text that discusses objects in orbit, and it includes buttons for viewing a satellite, the moon, and a telescope. The satellite button is selected and a 3D satellite is displayed.](https://docs-assets.developer.apple.com/published/0b838d64969702add7598ad8241b969f/visionos-window-2d-with-volume@2x.png)A window containing 3D content**Prefer using a standard window to present a familiar interface and to support familiar tasks.** Help people feel at home in your app by displaying an interface they’re already comfortable with, reserving more immersive experiences for the meaningful content and activities you offer. For guidance, see [Immersive experiences](/design/human-interface-guidelines/immersive-experiences)
. If you want to showcase bounded 3D content like a game board, consider using a volume.

**Choose an initial window size that minimizes empty areas within it.** Too many empty areas can make a window look unnecessarily large while also obscuring other content in people’s space.

**Aim for a default shape that suits a window’s content.** For example, a default Keynote window is wide because slides are wide; a default Safari window is tall because most webpages are much longer than they are wide.

**Let people resize app windows when possible.** People appreciate being able to resize windows as they customize their space. If it makes sense, you can set minimum and maximum size values to help ensure that a window remains functional and looks good when people resize it.

**Look for moments or content in your app that people might want to immerse themselves in.** Even if your app uses mostly windows, there may be features that are enhanced when immersive. In the Photos app, for example, people open a panorama in an expanded view that can make them feel like they’re in the photo. For guidance, see [Immersive experiences](/design/human-interface-guidelines/immersive-experiences)
.

**Always ensure that the visual bounds of a window match the size of its containing scene.** If a scene exceeds the visible size of a window, window controls can appear misplaced and the window might not look the way people expect it to, making it difficult to interact with. For developer guidance, see [`Scene`](/documentation/SwiftUI/Scene)
.

#### [Volumes](/design/human-interface-guidelines/windows#Volumes)

A volume has a horizontal base and helps you display 3D content that people can view from any angle, like a globe.

![A screenshot of a volume containing a 3D globe in visionOS, beside a window.](https://docs-assets.developer.apple.com/published/abd638cdf19eac59b94e00b399995e63/visionos-window-3d@2x.png)A volumeVolumes and windows share a few similarities:

* In the Shared Space, the system determines the initial position of a volume, just as it does with a window.
* A volume provides the same management controls that people use to reposition or close a window.
* A volume can use a [glass](/design/human-interface-guidelines/materials#visionOS)
 background.

Volumes and windows differ in the type of scaling the system applies: visionOS automatically uses dynamic scaling with a window, but fixed scaling with a volume.

**Prefer using a volume to display rich, 3D content.** If you want to present a familiar, UI-centric interface, it generally works best to use a window.

[Resources](/design/human-interface-guidelines/windows#Resources)
-----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/windows#Related)

[Split views](/design/human-interface-guidelines/split-views)


[Multitasking](/design/human-interface-guidelines/multitasking)


#### [Developer documentation](/design/human-interface-guidelines/windows#Developer-documentation)

[`Scene`](/documentation/SwiftUI/Scene)


[`WindowGroup`](/documentation/SwiftUI/WindowGroup)


[`NSWindow`](/documentation/appkit/nswindow)


#### [Videos](/design/human-interface-guidelines/windows#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/38E4EE32-29B5-4478-B8B6-35B8ACA67B16/8130_wide_250x141_1x.jpg) Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_1x.jpg) Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072) 
[Change log](/design/human-interface-guidelines/windows#Change-log)
-------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |

