# **[components-layout-and-organization] disclosure-controls**

## Disclosure controls reveal and hide information and functionality related to specific controls or views.
> 공개 제어는 특정 제어 또는 뷰와 관련된 정보 및 기능을 공개하고 숨긴다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/disclosure-control-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/disclosure-control-intro-dark_2x.png)

# **Best practices**

**Use a disclosure control to hide details until they’re relevant.** Place controls that people are most likely to use at the top of the disclosure hierarchy so they’re always visible, with more advanced functionality hidden by default. This organization helps people first focus on the most essential information without overwhelming them with too many detailed options.
> 노출 컨트롤을 사용하여 관련될 때까지 세부 정보를 숨깁니다. 사용자가 가장 많이 사용하는 컨트롤을 노출 계층 맨 위에 배치하여 항상 볼 수 있도록 하고 고급 기능은 기본적으로 숨겨 둡니다. 이 조직은 사람들이 너무 많은 세부 옵션으로 압도하지 않고 가장 필수적인 정보에 먼저 집중할 수 있도록 도와줍니다.
>




# **Disclosure triangles**

A disclosure triangle shows and hides information and functionality associated with a view or a list of items. For example, Keynote uses a disclosure triangle to show advanced options when exporting a presentation, and the Finder uses disclosure triangles to progressively reveal hierarchy when navigating a folder structure in list view.
> 노출 삼각형은 보기 또는 항목 목록과 관련된 정보 및 기능을 표시하고 숨깁니다. 예를 들어, Keynote는 프리젠테이션을 내보낼 때 공개 삼각형을 사용하여 고급 옵션을 표시하고, Finder는 목록 보기에서 폴더 구조를 탐색할 때 공개 삼각형을 사용하여 계층을 점진적으로 표시합니다.
>




• [Collapsed](../components/layout-and-organization/disclosure-controls#)
• [Expanded](../components/layout-and-organization/disclosure-controls#)

-

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/disclosure-controls/images/disclosure-triangle-before_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/disclosure-controls/images/disclosure-triangle-before_2x.png)


A disclosure triangle points inward from the leading edge when its content is hidden and down when its content is visible. Clicking or tapping the disclosure triangle switches between these two states, and the view expands or collapses accordingly to accommodate the content.
> 공개 삼각형은 내용이 숨겨져 있을 때는 앞쪽 가장자리에서 안쪽을 가리키고 내용이 보일 때는 아래쪽을 가리킵니다. 공개 삼각형을 클릭하거나 탭하면 이 두 상태 간에 전환되며, 그에 따라 보기가 확장되거나 축소되어 콘텐츠를 수용할 수 있습니다.
>




**Provide a descriptive label when using a disclosure triangle.** Make sure your labels indicate what is disclosed or hidden, like “Advanced Options.”
> 노출 삼각형을 사용할 때는 설명 레이블을 지정합니다. 레이블에 "고급 옵션"과 같이 노출되거나 숨겨진 항목이 표시되었는지 확인하십시오.
>




For developer guidance, see [NSBezelStyleDisclosure](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstyledisclosure).

# **Disclosure buttons**

A disclosure button shows and hides functionality associated with a specific control. For example, the macOS Save sheet shows a disclosure button next to the Save As text field. When people click or tap this button, the Save dialog expands to give advanced navigation options for selecting an output location for their document.
> 노출 버튼은 특정 컨트롤과 관련된 기능을 보여주고 숨긴다. 예를 들어 macOS 저장 시트는 다른 이름으로 저장 텍스트 필드 옆에 노출 버튼을 표시합니다. 사용자가 이 단추를 누르거나 누르면 저장 대화상자가 확장되어 문서의 출력 위치를 선택할 수 있는 고급 네비게이션 선택사항을 제공합니다.
>




• [Collapsed](../components/layout-and-organization/disclosure-controls#)
• [Expanded](../components/layout-and-organization/disclosure-controls#)

-

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/disclosure-controls/images/disclosure-button-before_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/disclosure-controls/images/disclosure-button-before_2x.png)


A disclosure button points down when its content is hidden and up when its content is visible. Clicking or tapping the disclosure button switches between these two states, and the view expands or collapses accordingly to accommodate the content.
> 노출 버튼은 콘텐츠가 숨겨져 있을 때 아래를 가리키고 콘텐츠가 보일 때 위로 향합니다. 공개 버튼을 클릭하거나 탭하면 이 두 가지 상태가 전환되고, 그에 따라 보기가 확장되거나 축소되어 콘텐츠를 수용할 수 있습니다.
>




**Place a disclosure button near the content that it shows and hides.**Establish a clear relationship between the control and the expanded choices that appear when a person clicks or taps a button.
> 표시 및 숨기는 내용 근처에 노출 버튼을 놓습니다.사용자가 단추를 클릭하거나 누를 때 나타나는 컨트롤과 확장된 선택 항목 사이에 명확한 관계를 설정합니다.
>




**Use no more than one disclosure button in a single view.** Multiple disclosure buttons add complexity and can be confusing.
> 단일 뷰에서 노출 버튼을 하나만 사용하십시오. 노출 버튼이 여러 개 있으면 복잡해지고 혼란스러울 수 있습니다.
>




For developer guidance, see [NSBezelStyleRoundedDisclosure](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstyleroundeddisclosure).

# **Platform considerations**

*No additional considerations for macOS. Not supported in tvOS or watchOS.*
> macOS에 대한 추가 고려 사항은 없습니다. tvOS 또는 시계에서 지원되지 않음OS.
>




# **iOS, iPadOS**

Disclosure controls are available in iOS and iPadOS with the SwiftUI [DisclosureGroup](https://developer.apple.com/documentation/swiftui/disclosuregroup) view.
> iOS 및 iPad에서 공개 제어 사용 가능스위프트가 탑재된 OSUI 노출 그룹 보기.
>



