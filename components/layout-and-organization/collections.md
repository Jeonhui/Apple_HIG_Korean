# **[components-layout-and-organization] collections**

## A collection manages an ordered set of content and presents it in a customizable and highly visual layout.
> 컬렉션은 정렬된 콘텐츠 집합을 관리하고 사용자 정의 가능하고 시각적 효과가 높은 레이아웃으로 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/collection-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/collection-view-intro-dark_2x.png)

Generally speaking, collections are ideal for showing image-based content.
> 일반적으로 이미지 기반 콘텐츠를 표시하는 데 컬렉션이 이상적입니다.
>




# **Best practices**

**Use the standard row or grid layout whenever possible.** Collections display content by default in a horizontal row or a grid, which are simple, effective appearances that people expect. Avoid creating a custom layout that might confuse people or draw undue attention to itself.
> 가능한 경우 항상 표준 행 또는 그리드 레이아웃을 사용합니다. 컬렉션은 기본적으로 콘텐츠를 수평 행 또는 그리드에 표시하며, 이는 사람들이 기대하는 단순하고 효과적인 모양입니다. 사용자를 혼란스럽게 하거나 자신에게 과도한 주의를 끌 수 있는 사용자 정의 레이아웃을 만들지 마십시오.
>




**Consider using a table instead of a collection for text.** It’s generally simpler and more efficient to view and digest textual information when it’s displayed in a scrollable list.
> 텍스트 모음 대신 표를 사용하는 것이 좋습니다. 텍스트 정보가 스크롤 가능한 목록에 표시될 때 일반적으로 더 간단하고 더 효율적으로 보고 요약할 수 있습니다.
>




**Make it easy to choose an item.** If it’s too difficult to get to an item in your collection, people will get frustrated and lose interest before reaching the content they want. Use adequate padding around images to keep focus clear and prevent content from overlapping.
> 항목을 쉽게 선택할 수 있습니다. 컬렉션에 있는 항목을 찾는 것이 너무 어렵다면, 사람들은 그들이 원하는 내용에 도달하기 전에 좌절하고 흥미를 잃을 것입니다. 초점을 선명하게 유지하고 콘텐츠가 겹치지 않도록 하려면 이미지 주위에 적절한 패딩을 사용하십시오.
>




**Add custom interactions when necessary.** By default, people can tap to select, touch and hold to edit, and swipe to scroll. If your app requires it, you can add more gestures for performing custom actions.
> 필요에 따라 사용자 지정 상호 작용을 추가합니다. 기본적으로 사용자는 선택하기 위해 누르고, 편집하기 위해 길게 누르고, 스크롤하기 위해 스와이프할 수 있습니다. 앱에 필요한 경우 사용자 지정 작업을 수행하기 위한 제스처를 추가할 수 있습니다.
>




**Consider using animations to provide feedback when people insert, delete, or reorder items.** Collections support standard animations for these actions, and you can also use custom animations.
> 사용자가 항목을 삽입하거나 삭제하거나 순서를 변경할 때 애니메이션을 사용하여 피드백을 제공하는 것이 좋습니다. 컬렉션은 이러한 작업에 대한 표준 애니메이션을 지원하며 사용자 지정 애니메이션을 사용할 수도 있습니다.
>




# **Platform considerations**

*No additional considerations for macOS or tvOS. Not supported in watchOS.*
> macOS 또는 tvOS에 대한 추가 고려 사항 없음. 시계에서 지원되지 않음OS.
>




# **iOS, iPadOS**

**Use caution when making dynamic layout changes.** The layout of a collection can change dynamically. Be sure any changes make sense and are easy to track. If possible, try to avoid changing the layout while people are viewing and interacting with it, unless it’s in response to an explicit action.
> 동적 레이아웃을 변경할 때는 주의하십시오. 컬렉션의 레이아웃은 동적으로 변경될 수 있습니다. 변경사항이 타당하고 추적하기 쉽도록 하십시오. 가능한 경우, 명시적인 작업에 대한 응답이 아닌 경우, 사용자가 레이아웃을 보고 상호 작용하는 동안 레이아웃을 변경하지 않도록 하십시오.
>



