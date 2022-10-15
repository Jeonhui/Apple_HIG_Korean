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

**Present content modally only when there’s a clear benefit.** A modal experience takes people out of their current context and requires an action to dismiss, so it’s important to use modality only when it helps people focus or make choices that affect their content or device.
> 분명한 이점이 있을 때만 콘텐츠를 모듈식으로 제시합니다. 모달 경험은 사람들을 현재 상황에서 벗어나게 하고 무시할 행동을 요구하므로 사람들이 집중하거나 콘텐츠나 장치에 영향을 미치는 선택을 하는 데 도움이 되는 경우에만 모달리티를 사용하는 것이 중요합니다.
>




**Aim to keep modal tasks simple, short, and narrowly focused.** If a modal task is too complicated, people can lose track of the task they suspended when they entered the modal view, especially if the modal view obscures their previous context.
> 모달 작업을 단순하고, 짧고, 좁게 초점을 맞추는 것을 목표로 한다. 모달 작업이 너무 복잡하면 특히 모달 보기가 이전 컨텍스트를 흐리게 하는 경우 사람들이 모달 보기에 들어갔을 때 일시 중단한 작업을 추적할 수 없다.
>




**Take care to avoid creating a modal experience that feels like an app within your app.** In particular, presenting a hierarchy of views within a modal task can make people forget how to retrace their steps. If a modal task must contain subviews, provide a single path through the hierarchy and avoid including buttons that people might mistake for the button that dismisses the modal view.
> 앱 내에서 앱처럼 느껴지는 모달 경험을 만들지 않도록 주의하십시오. 특히, 모달 작업 내에서 뷰의 계층을 제시하는 것은 사람들로 하여금 자신의 단계를 되돌리는 방법을 잊게 할 수 있다. 모달 태스크에 하위 보기가 있어야 하는 경우, 계층 구조를 통과하는 단일 경로를 제공하고 모달 보기를 해제하는 단추로 오인할 수 있는 단추를 포함하지 않도록 합니다.
>




**Consider using a full-screen modal style for immersive content or a complex task.** A modal experience that fills the display or a window minimizes distractions, so it can work well for presenting videos, photos, or camera views, or to enable a multistep task like marking up a document or editing a photo.
> 몰입형 콘텐츠 또는 복잡한 작업에 전체 화면 모달 스타일을 사용하는 것을 고려해 보십시오. 디스플레이 또는 창을 채우는 모달 경험은 산만함을 최소화하므로 비디오, 사진 또는 카메라 뷰를 표시하거나 문서 표시 또는 사진 편집과 같은 다단계 작업을 수행할 수 있습니다.
>




**Always give people an obvious way to dismiss a modal view.** In general, it works well to follow the platform conventions people already know. For example, in iOS, iPadOS, and watchOS apps, people typically expect to find a button in the navigation bar or swipe down; in macOS and tvOS apps, people expect to find a button in the main content view.
> 항상 사람들에게 모달 뷰를 무시할 수 있는 분명한 방법을 제공하세요. 일반적으로 사람들이 이미 알고 있는 플랫폼 규약을 따르는 것이 효과가 좋다. 예를 들어 iOS, iPadOS 및 watch에서OS 앱은 일반적으로 네비게이션 바에서 버튼을 찾거나 아래로 스와이프할 것으로 예상되며, macOS와 tvOS 앱에서는 메인 콘텐츠 뷰에서 버튼을 찾을 것으로 예상한다.
>




**When necessary, help people avoid data loss by getting confirmation before closing a modal view.** Regardless of whether people use a dismiss gesture or a button, if closing the view could result in the loss of user-generated content, be sure to explain the situation and give people ways to resolve it. For example, in iOS, you might present an action sheet that includes a save option.
> 필요한 경우 모달 보기를 닫기 전에 확인을 받아 데이터 손실을 방지할 수 있습니다. 사람들이 무시 제스처를 사용하든 버튼을 사용하든 간에 보기를 닫으면 사용자가 생성한 콘텐츠가 손실될 수 있다면 상황을 설명하고 해결 방법을 제공해야 한다. 예를 들어 iOS에서 저장 옵션이 포함된 작업 시트를 표시할 수 있습니다.
>




**Make it easy to identify a modal view’s task.** When people enter a modal view, they switch away from their previous context and might not return to it right away. When you provide a title that names the modal view’s task — or additional text that describes the task or provides guidance — you can help people keep their place in your app.
> 모달 뷰의 작업을 쉽게 식별할 수 있습니다. 사람들이 모달 뷰에 들어가면 이전 컨텍스트에서 벗어나 바로 돌아가지 않을 수 있습니다. 모달 보기의 작업 이름을 지정하는 제목이나 작업을 설명하거나 지침을 제공하는 추가 텍스트를 제공하는 경우 다른 사용자가 앱에서 자신의 위치를 유지하도록 도울 수 있습니다.
>




**Avoid presenting a modal view on top of another modal view.** Multiple modal views onscreen at the same time can be confusing because people must remember more than one previous context. Although an alert can appear on top of all other content to deliver critical information, having more than one alert onscreen at the same time is very confusing.
> 다른 모달 보기 위에 모달 보기를 표시하지 않도록 합니다. 동시에 화면의 여러 모달 뷰는 사람들이 둘 이상의 이전 컨텍스트를 기억해야 하기 때문에 혼란스러울 수 있다. 중요한 정보를 전달하기 위해 경고가 다른 모든 콘텐츠 위에 나타날 수 있지만 동시에 둘 이상의 경고를 화면에 표시하면 매우 혼란스럽습니다.
>



