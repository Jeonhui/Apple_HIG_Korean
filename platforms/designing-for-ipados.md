# **[Platforms] Designing for iPadOS**

### People value the power, mobility, and flexibility of iPad as they enjoy media, play games, perform detailed productivity tasks, and bring their creations to life.
> 사람들은 미디어를 즐기고, 게임을 하고, 세부적인 생산성 작업을 수행하고, 창작물을 생생하게 만들면서 아이패드의 힘, 이동성 및 유연성을 중요시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/platforms/platform-iPadOS-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/platforms/platform-iPadOS-intro-dark_2x.png)

As you begin designing your app or game for iPad, start by understanding the following fundamental device characteristics and patterns that distinguish the iPadOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app or game that iPad users appreciate.
> iPad용 앱이나 게임을 디자인하기 시작할 때 iPad를 구별하는 다음과 같은 기본 장치 특성과 패턴을 이해하는 것부터 시작하십시오.OS 경험. 이러한 특징과 패턴을 사용하여 디자인 결정을 알려주면 iPad 사용자가 높이 평가하는 앱이나 게임을 제공하는 데 도움이 될 수 있습니다.
>




**Display.** iPad has a large, high-resolution display.
> 디스플레이. iPad에는 대형 고해상도 디스플레이가 있습니다.
>




**Ergonomics.** People often hold their iPad while using it, but they might also set it on a surface or place it on a stand. Positioning the device in different ways can change the viewing distance, although people are typically within about 3 feet of the device as they interact with it.
> 인간공학. 사람들은 종종 아이패드를 사용하는 동안 그것을 잡지만, 그들은 그것을 표면에 놓거나 스탠드에 놓을 수도 있다. 기기를 서로 다른 방식으로 배치하면 시야 거리를 변경할 수 있지만 사람들은 기기와의 상호 작용 시 기기로부터 약 3피트 이내에 있다.
>




**Inputs.** People can interact with iPad using Multi-Touch [gestures](../inputs/touchscreen-gestures) and [onscreen keyboards](../components/selection-and-input/onscreen-keyboards), an attached [keyboard](../inputs/keyboards) or [pointing device](../inputs/pointing-devices), [Apple Pencil](../inputs/apple-pencil-and-scribble), or [voice](../technologies/siri/introduction), and they often combine multiple input modes.
> 입력. 멀티터치 제스처와 화면 키보드, 연결된 키보드 또는 포인팅 장치, Apple Pencil 또는 음성을 사용하여 iPad와 상호 작용할 수 있으며 여러 입력 모드를 결합하는 경우가 많습니다.
>




**App interactions.** Sometimes, people perform a few quick actions on their iPad. At other times, they spend hours immersed in games, media, content creation, or productivity tasks. People frequently have multiple apps open at the same time, and they appreciate viewing more than one app onscreen at once and taking advantage of inter-app capabilities like drag and drop.
> 앱 상호 작용. 때때로 사람들은 아이패드에서 몇 가지 빠른 동작을 수행합니다. 때로는 게임, 미디어, 콘텐츠 제작 또는 생산성 작업에 몰두하는 데 몇 시간을 소비하기도 한다. 사람들은 종종 동시에 여러 개의 앱을 열어놓고, 한 번에 두 개 이상의 앱을 보고 드래그 앤 드롭과 같은 앱 간 기능을 활용하는 것을 높이 평가한다.
>




**System features.** iPadOS provides several features that help people interact with the system and their apps in familiar, consistent ways.
> 시스템 기능. iPadOS는 사람들이 친숙하고 일관된 방식으로 시스템 및 앱과 상호 작용할 수 있도록 도와주는 몇 가지 기능을 제공합니다.
>




- [Multitasking](../patterns/multitasking)
- [Widgets](../components/system-experiences/widgets)
- [Drag and drop](../patterns/drag-and-drop)
- >  끌어서 놓기


# **Best practices**

Great iPad experiences integrate the platform and device capabilities that people value most. To help your experience feel at home in iPadOS, prioritize the following ways to incorporate these features and capabilities.
> 훌륭한 iPad 경험은 사람들이 가장 중요하게 생각하는 플랫폼과 장치 기능을 통합합니다. iPadOS에서 편안한 경험을 할 수 있도록 다음과 같은 기능을 통합하는 방법을 우선시하십시오.
>




- Take advantage of the large display to elevate the content people care about, minimizing modal interfaces and full-screen transitions, and positioning onscreen controls where they’re easy to reach, but not in the way.
- >  대형 디스플레이를 활용하여 사람들이 관심을 갖는 콘텐츠를 높이고, 모달 인터페이스와 전체 화면 전환을 최소화하며, 접근하기 쉽지만 방해가 되지 않는 곳에 화면 컨트롤을 배치합니다.

- Use viewing distance and input mode to help you determine the size and density of the onscreen content you display.
- >  표시 거리 및 입력 모드를 사용하여 표시되는 화면 콘텐츠의 크기와 밀도를 쉽게 확인할 수 있습니다.

- Let people use Multi-Touch gestures, a physical keyboard or trackpad, or Apple Pencil, and consider enabling unique interactions that combine multiple input modes.
- >  사람들이 멀티터치 제스처, 실제 키보드나 트랙패드 또는 Apple Pencil을 사용하도록 하고 여러 입력 모드를 결합하는 고유한 상호 작용을 사용하도록 고려합니다.

- Adapt seamlessly to appearance changes — like device orientation, multitasking modes, Dark Mode, and Dynamic Type — and transition effortlessly to running in macOS, letting people choose the configurations that work best for them.
- >  장치 방향, 멀티태스킹 모드, 다크 모드 및 동적 유형과 같은 외관 변화에 원활하게 적응하고 macOS에서 실행하는 것으로 쉽게 전환하여 사람들이 자신에게 가장 적합한 구성을 선택할 수 있도록 합니다.

