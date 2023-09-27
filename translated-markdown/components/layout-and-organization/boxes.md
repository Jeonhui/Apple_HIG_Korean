# **[components-layout-and-organization] boxes**

## A box creates a visually distinct group of logically related information and components.
> 상자는 논리적으로 관련된 정보와 구성 요소의 시각적으로 구별되는 그룹을 만듭니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/box-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/box-intro-dark_2x.png)

By default, a box uses a visible border or background color to separate its contents from the rest of the interface. A box can also include a title.
> 기본적으로 상자는 표시 가능한 테두리 또는 배경색을 사용하여 인터페이스의 나머지 부분과 내용을 구분합니다. 상자에는 제목을 포함할 수도 있습니다.
>




# **Best practices**

**Prefer keeping a box relatively small in comparison with its containing view.** As a box’s size gets close to the size of the containing window or screen, it becomes less effective at communicating the separation of grouped content, and it can crowd other content.
> 상자의 크기가 포함된 창이나 화면 크기에 가까울수록 그룹화된 내용을 구분하는 데 효과적이지 않고 다른 콘텐츠가 몰릴 수 있습니다.
>




**Consider using padding and alignment to communicate additional grouping within a box.** A box’s border is a distinct visual element — adding nested boxes to define subgroups can make your interface feel busy and constrained.
> 상자 내에서 추가 그룹화를 전달하기 위해 패딩 및 정렬을 사용하는 것을 고려해 보십시오. 상자의 테두리는 뚜렷한 시각적 요소입니다. 하위 그룹을 정의하기 위해 중첩된 상자를 추가하면 인터페이스가 바쁘고 제약된 것처럼 느껴질 수 있습니다.
>




# **Content**

**Provide a succinct introductory title if it helps clarify the box’s contents.** The appearance of a box helps people understand that its contents are related, but it might make sense to provide more detail about the relationship. Also, a title can help VoiceOver users predict the content they encounter within the box.
> 상자의 내용을 명확히 하는 데 도움이 되는 간단한 소개 제목을 제공하십시오. 상자의 모양은 사람들이 상자의 내용이 관련이 있다는 것을 이해하는 데 도움이 되지만 관계에 대해 더 자세히 설명하는 것이 이치에 맞을 수 있습니다. 또한 제목은 VoiceOver 사용자가 상자 내에서 접하는 내용을 예측하는 데 도움이 될 수 있습니다.
>




**If you need a title, write a brief phrase that describes the contents.** Use sentence-style capitalization. Avoid ending punctuation unless you use a box in a settings pane, where you append a colon to the title.
> 제목이 필요하면 내용을 설명하는 간단한 구절을 쓰십시오. 문장 형식의 대문자를 사용하십시오. 제목에 콜론을 추가하는 설정 영역에서 상자를 사용하지 않는 경우 구두점을 종료하지 마십시오.
>




# **Platform considerations**

*Not supported in tvOS or watchOS.*
> tvOS 또는 시계에서 지원되지 않음OS.
>




# **iOS, iPadOS**

By default, iOS and iPadOS use the secondary and tertiary background [colors](../foundations/color)in boxes.
> 기본적으로 iOS 및 iPadOS는 박스에 2차 및 3차 배경색을 사용한다.
>




# **macOS**

By default, macOS displays a box’s title above it.
> 기본적으로 macOS는 상자 위에 상자 제목을 표시합니다.
>



