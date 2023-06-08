# **[components-selection-and-input] segmented-controls**

## A segmented control is a linear set of two or more segments, each of which functions as a button.
> 세그먼트화된 컨트롤은 두 개 이상의 세그먼트로 구성된 선형 집합으로, 각 세그먼트는 버튼으로 작동합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/segmented-control-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/segmented-control-intro-dark_2x.png)

Within a segmented control, all segments are usually equal in width. Like buttons, segments can contain text or images. Segments can also have text labels beneath them (or beneath the control as a whole).
> 세그먼트화된 컨트롤 내에서는 일반적으로 모든 세그먼트의 너비가 동일합니다. 버튼과 마찬가지로 세그먼트에도 텍스트 또는 이미지가 포함될 수 있습니다. 세그먼트 아래(또는 전체 컨트롤 아래)에 텍스트 레이블이 있을 수도 있습니다.
>




# **Best practices**

A segmented control can enable a single choice or multiple choices. For example, in Keynote people can select only one segment in the alignment options control to align selected text. In contrast, people can choose multiple segments in the font attributes control to enable combinations of boldface, italics, and underline. The toolbar of a Keynote window also uses a segmented control to let people show and hide various editing panes within the main window area.
> 세그먼트화된 제어는 단일 선택 또는 다중 선택을 가능하게 한다. 예를 들어, 키노트에서 사용자는 정렬 옵션 컨트롤에서 선택한 텍스트를 정렬할 세그먼트를 하나만 선택할 수 있습니다. 대조적으로, 사람들은 글꼴 속성 컨트롤에서 여러 세그먼트를 선택하여 굵은 글씨, 기울임꼴 및 밑줄을 조합할 수 있습니다. 또한 키노트 창의 도구 모음은 세그먼트화된 컨트롤을 사용하여 기본 창 영역 내에서 다양한 편집 창을 표시하거나 숨길 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/segmented-controls/images/segmented-control-one-choice_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/segmented-controls/images/segmented-control-one-choice_2x.png)

Single choice

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/segmented-controls/images/segmented-control-multiple-choices_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/segmented-controls/images/segmented-control-multiple-choices_2x.png)

Multiple choices

**Use a segmented control to provide closely related choices that affect an object, state, or view.** For example, a segmented control can help people switch between views in a toolbar. Avoid using a segmented control to enable actions, such as adding, removing, or editing content.
> 세그먼트화된 컨트롤을 사용하여 개체, 상태 또는 보기에 영향을 미치는 밀접한 관련된 선택사항을 제공합니다. 예를 들어, 세그먼트화된 컨트롤은 사용자가 도구 모음에서 보기를 전환하는 데 도움이 될 수 있습니다. 세그먼트화된 컨트롤을 사용하여 콘텐츠 추가, 제거 또는 편집과 같은 작업을 활성화하지 마십시오.
>




**Avoid crowding the control with too many segments.** Too many segments can be hard to parse and time-consuming to navigate. Aim for no more than about five to seven segments in a wide interface and no more than about five segments on iPhone.
> 세그먼트가 너무 많으면 컨트롤이 너무 붐비지 않도록 합니다. 세그먼트가 너무 많으면 구문 분석이 어렵고 탐색하는 데 시간이 많이 걸릴 수 있습니다. 넓은 인터페이스에서 약 5~7개의 세그먼트를 목표로 하고 아이폰에서는 약 5개의 세그먼트를 목표로 합니다.
>




**In general, keep segment size consistent.** When all segments have equal width, a segmented control feels balanced. To the extent possible, it’s best to keep icon and title widths consistent too.
> 일반적으로 세그먼트 크기를 일정하게 유지하십시오. 모든 세그먼트의 너비가 동일하면 세그먼트화된 컨트롤이 균형을 유지하는 것처럼 느껴집니다. 아이콘과 제목 너비도 가능한 한 일정하게 유지하는 것이 좋습니다.
>




# **Content**

**Prefer using either text or images — not a mix of both — in a single segmented control.** Although individual segments can contain text labels or images, mixing the two in a single control can lead to a disconnected and confusing interface.
> 단일 세그먼트 컨트롤에서 텍스트 또는 이미지를 사용하는 것이 좋습니다. 개별 세그먼트에는 텍스트 레이블이나 이미지가 포함될 수 있지만 단일 컨트롤에서 두 가지를 혼합하면 인터페이스가 연결되지 않고 혼동될 수 있습니다.
>




**As much as possible, use content with a similar size in each segment.**Because all segments typically have equal width, it doesn’t look good if content fills some segments but not others.
> 가능한 각 세그먼트에서 비슷한 크기의 콘텐츠를 사용하십시오.일반적으로 모든 세그먼트의 너비가 동일하기 때문에 일부 세그먼트는 내용이 채워지지만 다른 세그먼트는 채워지지 않으면 보기에 좋지 않습니다.
>




**Use nouns or noun phrases for segment labels.** Write text that describes each segment and uses title-style capitalization. A segmented control that displays text labels doesn’t need introductory text.
> 세그먼트 레이블에는 명사 또는 명사 구를 사용합니다. 각 세그먼트를 설명하고 제목 스타일의 대문자를 사용하는 텍스트를 작성합니다. 텍스트 레이블을 표시하는 세그먼트화된 컨트롤에는 소개 텍스트가 필요하지 않습니다.
>




# **Platform considerations**

*Not supported in watchOS.*

# **iOS, iPadOS**

**Use a segmented control in a bar only as recommended.** Specifically, if you use a segmented control in a navigation bar, avoid including any other controls or a title. Avoid using a segmented control in a toolbar, because toolbar items act on the current screen — they don’t let people switch contexts.
> 권장되는 경우에만 막대에 세그먼트 컨트롤을 사용하십시오. 특히 탐색 막대에 세그먼트 컨트롤을 사용하는 경우 다른 컨트롤이나 제목을 포함하지 마십시오. 도구 모음 항목은 현재 화면에서 작동하므로 사용자가 컨텍스트를 전환할 수 없으므로 도구 모음에서 세그먼트화된 컨트롤을 사용하지 마십시오.
>




# **macOS**

**Consider using introductory text to clarify the purpose of a segmented control.** When the control uses symbols or interface icons, you could also add a label below each segment to clarify its meaning. If your app includes help tags, provide a help tag for each segment in a segmented control.
> 소개 텍스트를 사용하여 세그먼트화된 컨트롤의 목적을 명확히 하는 것을 고려하십시오. 컨트롤이 기호나 인터페이스 아이콘을 사용하는 경우 각 세그먼트 아래에 레이블을 추가하여 의미를 명확히 할 수도 있습니다. 앱에 도움말 태그가 포함된 경우 세그먼트화된 컨트롤의 각 세그먼트에 대한 도움말 태그를 제공합니다.
>




**Use a tab view in the main window area — instead of a segmented control — for view switching.** A [tab view](../components/layout-and-organization/tab-views) is similar in appearance to a [box](../components/layout-and-organization/boxes)combined with a segmented control, and enables efficient view switching. Consider using a segmented control to enable view-switching in a toolbar or inspector pane.
> 보기 전환에는 세그먼트화된 컨트롤 대신 주 창 영역의 탭 보기를 사용합니다. 탭 보기는 세그먼트화된 컨트롤과 결합된 상자 모양과 유사하며 효율적인 보기 전환을 가능하게 합니다. 세그먼트 컨트롤을 사용하여 도구 모음 또는 검사기 창에서 보기 전환을 사용하는 것이 좋습니다.
>




**Size custom interface icons appropriately based on the size of the control.** Use the following values for guidance.
> 컨트롤 크기에 따라 사용자 지정 인터페이스 아이콘의 크기를 적절하게 조정하십시오. 다음 값을 사용하여 지침을 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/segmented-controls/images/segmented-control-icons-regular_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/segmented-controls/images/segmented-control-icons-regular_2x.png)

Regular

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/segmented-controls/images/segmented-control-icons-small_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/segmented-controls/images/segmented-control-icons-small_2x.png)

Small

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/segmented-controls/images/segmented-control-icons-mini_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/segmented-controls/images/segmented-control-icons-mini_2x.png)

Mini

| Control size | Icon size |
| --- | --- |
| Regular | 17x17 px @1x (34x34 px @2x) |
| Small | 14x13 px @1x (28x26 px @2x) |
| Mini | 12x11 px @1x (24x22 px @2x) |

**Consider enabling spring loading.** On a Mac equipped with a Magic Trackpad, spring loading lets people activate a segment by dragging selected items over it and force clicking without dropping the selected items. People can also continue dragging the items after a segment activates.
> 매직 트랙패드가 장착된 Mac에서는 스프링 로드를 사용하여 선택한 항목을 끌어 세그먼트를 활성화하고 선택한 항목을 떨어뜨리지 않고 강제로 클릭할 수 있습니다. 세그먼트가 활성화된 후에도 항목을 계속 끌 수 있습니다.
>




# **tvOS**

**Consider using a split view instead of a segmented control on screens that perform content filtering.** People generally find it easy to navigate back and forth between content and filtering options using a split view. Depending on its placement, a segmented control may not be as easy to access.
> 콘텐츠 필터링을 수행하는 화면에서 세그먼트화된 컨트롤 대신 분할 보기를 사용하는 것을 고려해 보십시오. 일반적으로 사람들은 분할 보기를 사용하여 콘텐츠와 필터링 옵션을 앞뒤로 탐색하는 것이 쉽습니다. 위치에 따라 세그먼트화된 컨트롤은 액세스하기가 쉽지 않을 수 있습니다.
>




**Avoid putting other focusable elements close to segmented controls.**Segments become selected when focus moves to them, not when people click them. Carefully consider where you position a segmented control relative to other interface elements. If other focusable elements are too close, people might accidentally focus on them when attempting to switch between segments.
> 다른 초점 요소를 세그먼트 조정기에 가까이 두지 마십시오.사용자가 세그먼트를 클릭할 때가 아니라 포커스가 세그먼트로 이동할 때 세그먼트가 선택됩니다. 다른 인터페이스 요소와 비교하여 세그먼트화된 컨트롤의 위치를 신중하게 고려하십시오. 다른 초점 요소가 너무 가까우면 세그먼트 간 전환을 시도할 때 사람들이 실수로 초점을 맞출 수 있습니다.
>



