# **[patterns] offering-help**

# Although the most effective experiences are approachable and intuitive, you can provide contextual help when necessary.
> 가장 효과적인 경험은 접근 가능하고 직관적이지만 필요할 때 상황에 맞는 도움을 제공할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-offering-help-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-offering-help-intro-dark_2x.png)

# **Best practices**

**Let the tasks you enable inform the types of help people might need.** For example, you might help people perform simple, one- or two-step tasks by displaying an inline view that succinctly describes the task. In contrast, if your app or game enables complex or multistep tasks you might want to provide a tutorial that teaches people how to accomplish larger goals. In general, directly relate the help you provide to the precise action or task people are doing right now and make it easy for people to dismiss or avoid the help if they don’t need it.
> 사용 가능한 태스크가 사용자에게 필요한 도움말 유형을 알려주도록 합니다. 예를 들어, 태스크를 간결하게 설명하는 인라인 보기를 표시하여 사용자가 간단한 1단계 또는 2단계 태스크를 수행할 수 있도록 지원할 수 있습니다. 대조적으로, 당신의 앱이나 게임이 복잡하거나 다단계 작업을 가능하게 한다면, 당신은 사람들에게 더 큰 목표를 달성하는 방법을 알려주는 자습서를 제공하고 싶을 것이다. 일반적으로, 여러분이 제공하는 도움을 사람들이 지금 하고 있는 정확한 행동이나 임무와 직접적으로 연관시키고, 사람들이 도움이 필요하지 않을 때 쉽게 거절하거나 피할 수 있도록 하세요.
>




**Use relevant and consistent language and images in your help content.** Always make sure guidance is appropriate for the current context. For example, if someone’s using the Siri Remote with your tvOS experience, don’t show tips or images that feature a game controller. Also be sure the terms and descriptions you use are consistent with the platform. For example, don’t write copy that tells people to click a button on an iPhone or tap a menu item on a Mac.
> 도움말 콘텐츠에 적절하고 일관된 언어와 이미지를 사용합니다. 항상 지침이 현재 상황에 적합한지 확인하십시오. 예를 들어, 누군가가 TVOS 환경에서 Siri Remote를 사용하고 있다면 게임 컨트롤러가 포함된 팁이나 이미지를 보여주지 마십시오. 또한 사용하는 용어와 설명이 플랫폼과 일치하는지 확인하십시오. 예를 들어, iPhone에서 단추를 클릭하거나 Mac에서 메뉴 항목을 누르라는 내용의 사본을 작성하지 마십시오.
>




**Make sure all help content is inclusive.** For guidance, see [Inclusion](../foundations/inclusion/).
> 모든 도움말 내용이 포함되었는지 확인합니다. 자세한 내용은 포함을 참조하십시오.
>




**Avoid bloating your help content by explaining how standard components or patterns work.** Instead, focus on describing the specific action or task that a standard element enables in your app or game. If your experience introduces a unique control or expects people to use an input device in a nonstandard way — such as holding the Siri Remote rotated 90 degrees — orient people quickly, preferring animation or graphics to educate instead of a lengthy description.
> 표준 구성요소 또는 패턴이 작동하는 방식을 설명하여 도움말 내용을 부풀리지 않도록 합니다. 대신, 표준 요소가 당신의 앱이나 게임에서 가능하게 하는 특정한 행동이나 작업을 설명하는 데 집중하세요. 사용자 경험이 고유한 컨트롤을 도입하거나 사용자가 Siri Remote를 90도 회전시키는 것과 같은 비표준적인 방식으로 입력 장치를 사용할 것으로 예상하는 경우, 긴 설명 대신 교육할 애니메이션이나 그래픽을 선호하여 신속하게 사용자를 조정합니다.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, tvOS, or watchOS.*
> iOS, iPadOS, tvOS 또는 시청에 대한 추가 고려 사항 없음OS.
>




# **macOS**

A help tag (also called a *tooltip*) displays a small, transient view that briefly describes how to use a component in the interface. In apps that run on a Mac — including iPhone and iPad apps — help tags can appear after the pointer hovers briefly over an element.
> 도움말 태그(도구 팁이라고도 함)는 인터페이스의 구성 요소를 사용하는 방법을 간략하게 설명하는 작은 임시 보기를 표시합니다. iPhone 및 iPad 앱을 포함하여 Mac에서 실행되는 앱에서는 포인터가 요소 위로 잠시 이동한 후에 도움말 태그가 나타날 수 있습니다.
>




**Focus only on the control that’s directly beneath the pointer.** When people want to know how to use a specific control, they don’t want to learn how to use nearby controls or how to perform a larger task.
> 포인터 바로 아래에 있는 컨트롤에만 초점을 맞춥니다. 특정 컨트롤을 사용하는 방법을 알고 싶을 때, 사람들은 근처의 컨트롤을 사용하는 방법이나 더 큰 작업을 수행하는 방법을 배우려고 하지 않습니다.
>




**Describe the action or task the control initiates.** It often works well to begin the description with a verb — for example, “Restore default settings” or “Add or remove a language from the list.”
> 컨트롤이 시작하는 작업 또는 작업에 대해 설명합니다. 예를 들어 "기본 설정 복원" 또는 "목록에서 언어 추가 또는 제거"와 같은 동사로 설명을 시작하는 것이 좋습니다.
>




**Be brief.** As much as possible, limit tag content to a maximum of 60 to 75 characters (note that localization often changes the length of text). To make a description brief and direct, consider using a sentence fragment and omitting articles. If you need a lot of text to describe a control, consider simplifying your interface design.
> 간략하게. 가능한 한 태그 내용을 최대 60~75자로 제한합니다(로컬라이제이션으로 텍스트 길이가 변경되는 경우가 있음). 간략하고 직접적인 설명을 위해 문장 파편을 사용하고 기사를 생략하는 것을 고려하십시오. 컨트롤을 설명하는 데 많은 텍스트가 필요한 경우 인터페이스 설계를 단순화하십시오.
>




**In general, avoid naming or referring to the component.** A help tag appears directly over the control, which usually provides sufficient context. Avoid defining a tag that does nothing but repeat the control’s title or label.
> 일반적으로 구성 요소의 이름을 지정하거나 참조하지 마십시오. 도움말 태그는 일반적으로 충분한 컨텍스트를 제공하는 컨트롤 위에 직접 나타납니다. 컨트롤의 제목이나 레이블을 반복하는 태그는 정의하지 마십시오.
>




**Consider offering context-sensitive help tags.** For example, you could provide different text for a control’s different states.
> 상황에 맞는 도움말 태그를 제공하는 것을 고려해 보십시오. 예를 들어 컨트롤의 여러 상태에 대해 다른 텍스트를 제공할 수 있습니다.
>



