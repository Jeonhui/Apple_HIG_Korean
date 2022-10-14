# **[patterns] modality**

# Modality is a design technique that presents content in a separate, focused mode that prevents interaction with the parent view and requires an explicit action to dismiss.
> 촬영장비는 상위 보기와의 상호 작용을 방지하고 명시적으로 작업을 수행해야 하는 별도의 집중 모드로 콘텐츠를 표시하는 설계 기법입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-modality-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-modality-intro-dark_2x.png)

Presenting content modally can:

- Ensure that people receive critical information and, if necessary, act on it
- >  사람들이 중요한 정보를 받고 필요한 경우 이에 따라 행동하도록 보장

- Provide options that let people confirm or modify their most recent action
- >  사용자가 최근 작업을 확인하거나 수정할 수 있는 옵션 제공

- Help people perform a distinct, narrowly scoped task without losing track of their previous context
- >  사람들이 이전의 맥락을 파악하지 않고 명확하고 좁은 범위의 작업을 수행할 수 있도록 지원

- Enable an immersive experience or help people focus on a complex task
- >  몰입형 환경을 지원하거나 복잡한 작업에 집중할 수 있도록 지원


Depending on the platform, you might use different components to present these types of modal experiences. For example, all platforms can present an *alert*, which is modal view that delivers important information related to your app or game. In addition, each platform may define various types of modal views for presenting context-specific options, such as *activity views,* *sheets*, and *confirmation dialogs* or *action sheets*. To help people perform a distinct task, iOS, iPadOS, and macOS apps tend to use sheets or popovers, but macOS and iPadOS apps might also just use a separate window.
> 플랫폼에 따라 다른 구성 요소를 사용하여 이러한 유형의 모달 경험을 표시할 수 있습니다. 예를 들어, 모든 플랫폼은 당신의 앱이나 게임과 관련된 중요한 정보를 전달하는 모달 뷰인 경고를 표시할 수 있다. 또한, 각 플랫폼은 활동 뷰, 시트 및 확인 대화 상자 또는 조치 시트와 같은 상황별 옵션을 제시하기 위한 다양한 유형의 모달 뷰를 정의할 수 있다. iOS, iPadOS 및 macOS 앱은 별도의 작업을 수행하기 위해 시트 또는 팝오버를 사용하는 경향이 있지만 macOS 및 iPadOS 앱은 별도의 창을 사용할 수도 있습니다.
>




To enable a temporary immersive experience, like viewing media, or to help people focus on a distinct, multistep task, like editing content, apps can offer a full-screen modal experience. In contrast, apps may also offer nonmodal types of full-screen experiences; for guidance, see [Going full screen](../patterns/going-full-screen).
> 미디어 보기와 같은 일시적인 몰입 경험을 가능하게 하거나 콘텐츠 편집과 같은 뚜렷하고 다단계 작업에 사람들이 집중할 수 있도록 돕기 위해 앱은 전체 화면 모달 경험을 제공할 수 있다. 이와는 대조적으로, 앱은 비모달 유형의 전체 화면 경험을 제공할 수도 있다.
>




# **Best practices**

