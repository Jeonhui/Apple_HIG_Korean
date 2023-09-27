# **[components-presentation] windows**

## A window contains the views and components that present the user interface of your app or game.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/window-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/window-intro-dark_2x.png)

Depending on the platform, device, and context, a window (or *scene*) can be undetectable. For example, in platforms where the default experience is full screen, like iOS, tvOS, and watchOS, people view and interact with the content inside a window — they don't view or interact with the window itself. In these cases, you don't need to design the appearance of the windows or scenes in your app or game. For developer guidance, see [Scene](https://developer.apple.com/documentation/swiftui/scene) and [UIWindow](https://developer.apple.com/documentation/uikit/uiwindow).

In contrast, iPadOS supports multitasking and multiple windows, so people can be aware of an app’s window as a visually distinct object. For example, people can view two or three apps onscreen at the same time or open multiple windows in the same app. To create a great iPadOS experience, you need to ensure that your windows and scenes look and behave the way people expect. For guidance, see [Multitasking](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking); for developer guidance, see [Scenes](https://developer.apple.com/documentation/uikit/app_and_environment/scenes).

In macOS, people are accustomed to interacting with app windows as distinct objects. Mac users typically run several apps at the same time, often viewing windows from multiple apps on one desktop and switching frequently between different windows — moving, resizing, minimizing, and revealing the windows to suit their work style. Even when people choose full-screen mode, which usually hides the window frame, the built-in, full-screen transition and the ability to reveal the toolbar remind them of the existence of the window.

**IMPORTANT**The guidance below applies to windows in macOS. For guidance on other types of window-like views in all platforms, see [Alerts](https://developer.apple.com/design/human-interface-guidelines/components/presentation/alerts), [Panels](https://developer.apple.com/design/human-interface-guidelines/components/presentation/panels),  [Popovers](https://developer.apple.com/design/human-interface-guidelines/components/presentation/popovers), and [Sheets](https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets).

# **macOS window anatomy**

A macOS window consists of a frame and a body area. People can move a window by dragging the frame and can often resize the window by dragging its edges.

![https://developer.apple.com/design/human-interface-guidelines/components/presentation/windows/images/window-anatomy_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/windows/images/window-anatomy_2x.png)

The *frame* is the portion of a window that surrounds body content. A window frame can include a title bar, [toolbar](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars), [tabs](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views), and (in rare cases) a bottom bar.

The window *body* displays the main content of the window. This content can fill the entire body area — such as a website in a Safari window or an image in Preview — or the content can display in multiple subviews, such as in a [split view](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views) interface. Content that extends beyond the bounds of views in the body area is scrollable.

# **macOS window states**

A macOS window can have one of three states:

- **Main.** The frontmost window that people focus on is an app’s main window. There can be only one main window per app.
- **Key.** Also called the active window, the key window accepts people’s input. There can be only one key window onscreen at a time. Although the front app’s main window is usually the key window, another window — such as a panel floating above the main window — might be key instead. People typically click a window to make it key; when people click an app’s Dock icon to bring all of that app’s windows forward, only the most recently accessed window becomes key.
- **Inactive.** A window that’s not in the foreground is an inactive window.

The system gives main, key, and inactive windows different appearances to help people visually identify them. For example, the key window uses color in the title bar options for closing, minimizing, and zooming; inactive windows and main windows that aren’t key use gray in these options. Also, inactive windows don’t use [vibrancy](https://developer.apple.com/design/human-interface-guidelines/foundations/materials) (an effect that can pull color into a window from the content underneath it), which makes them appear subdued and seem visually farther away than the main and key windows.

![https://developer.apple.com/design/human-interface-guidelines/components/presentation/windows/images/window-states_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/windows/images/window-states_2x.png)

**NOTE**Some windows — typically, panels like Colors or Fonts — become the key window only when people click the window's title bar or a component that requires keyboard input, such as a text field.

# **Best practices**

**Make sure your custom windows use the system-defined appearances.**People rely on the visual differences in various onscreen windows to help them identify the foreground window and know which window will accept their input. When you use system-provided components, a window’s background and button appearances update automatically when the window changes state; if you use custom implementations, you need to do this work yourself.

**Display a title unless the window’s content provides enough context to make one unnecessary.** For document windows, the title is the name of the document or *Untitled* (for new documents). For app windows, the title is the name of the app.

**If you need to use a filename as a title, make it easy to understand.** For example, use the file’s *display name,* which reflects people’s preference for showing or hiding a file extension and may be localized.

**Avoid including a file system path in the title bar.** Paths are generally too long to fit in the title bar without clipping, and they’re difficult for people to understand at a glance. If you need to show the complete path of a file or folder, do so in another way, like in an inspector pane.

**Use numeric suffixes to differentiate duplicate titles.** The first instance of a title doesn't need a numeric suffix. When other windows have the same title, append numeric suffixes, starting with *2*. For example, *Untitled*, *Untitled 2*, *Untitled 3*.

**Make sure people can still interact with your window if you hide the title bar.** Provide alternative ways — like menus — to close and minimize the window. Make sure people can still drag the frame to move the window. If the window has a toolbar and no title bar, make sure there’s enough space in the toolbar to drag the window without activating toolbar items.

**In general, use a dot to mark a modified document as unsaved only when it can't be autosaved.** If a document can be autosaved, you don't want to display a dot in the window's close button or next to the document’s name in the Window menu because doing so signals that people need to take action to save their changes. It’s fine to append a suffix like *Edited* to the document's title in the title bar, but you need to remove this suffix when it autosaves or if people manually perform a save.

**Use a bottom bar to display a small amount of information directly related to a window’s contents or to a selected item within it.** For example, Finder uses a bottom bar (called the Status Bar) to display the total number of items in a window, the number of selected items, and how much space is available on the disk. A bottom bar is small, so if you have more information to display, consider using an inspector, which typically presents information on the trailing side of a split view.

**Avoid putting critical information or actions in a bottom bar.** People often relocate a window in a way that hides its bottom edge.

# **Platform considerations**

*No additional considerations for iOS, macOS, tvOS, or watchOS.*

# **iPadOS**

To support multitasking and multiwindow workflows on iPad, you need to ensure that your windows adapt to different sizes and that you match each window's presentation style to its content. For guidance, see [Multitasking on iPad](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking#multitasking-on-ipad).