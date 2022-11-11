# **[components-layout-and-organization] tab-views**

## A tab view presents multiple mutually exclusive panes of content in the same area, which people can switch between using a tabbed control.
> 탭 보기는 동일한 영역에 서로 배타적인 여러 콘텐츠 창을 표시하며, 탭으로 된 컨트롤을 사용하여 전환할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/tab-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/tab-view-intro-dark_2x.png)

# **Best practices**

**Use a tab view to present closely related areas of content.** The appearance of a tab view provides a strong visual indication of enclosure. People expect each tab to display content that is in some way similar or related to the content in the other tabs.
> 탭 보기를 사용하여 밀접하게 관련된 내용 영역을 표시할 수 있습니다. 탭 보기의 모양은 인클로저를 시각적으로 강하게 나타냅니다. 사람들은 각 탭이 다른 탭의 내용과 비슷하거나 관련된 내용을 표시할 것으로 기대합니다.
>




**Make sure the controls within a pane affect content only in the same pane.** Panes are mutually exclusive, so ensure they’re fully self-contained.
> 창의 컨트롤이 동일한 창의 콘텐츠에만 영향을 미치는지 확인하십시오. 창은 상호 배타적이므로 완전히 독립되어 있는지 확인하십시오.
>




**Provide a label for each tab that describes the contents of its pane.** A good label helps people predict the contents of a pane before clicking or tapping its tab. In general, use nouns or short noun phrases for tab labels. A verb or short verb phrase may make sense in some contexts. Use title-style capitalization for tab labels.
> 창의 내용을 설명하는 각 탭에 레이블을 제공합니다. 좋은 레이블은 사용자가 탭을 클릭하거나 누르기 전에 창의 내용을 예측할 수 있도록 도와줍니다. 일반적으로 탭 레이블에는 명사 또는 짧은 명사 구문을 사용합니다. 동사나 짧은 동사 구절은 어떤 맥락에서 이치에 맞을 수 있다. 탭 레이블에는 제목 스타일 대문자화를 사용합니다.
>




**Avoid using a pop-up button to switch between tabs.** A tabbed control is efficient because it requires a single click or tap to make a selection, whereas a pop-up button requires two. A tabbed control also presents all choices onscreen at the same time, whereas people must click a pop-up button to see its choices. Note that a pop-up button can be a reasonable alternative in cases where there are too many panes of content to reasonably display with tabs.
> 탭으로 전환하려면 팝업 버튼을 사용하지 마십시오. 탭으로 된 컨트롤은 한 번의 클릭이나 탭으로 선택해야 하는 반면 팝업 버튼은 두 번을 선택해야 하기 때문에 효율적입니다. 또한 탭으로 된 컨트롤은 모든 선택 사항을 화면에 동시에 표시하는 반면, 사람들은 팝업 버튼을 클릭해야만 선택 사항을 볼 수 있다. 팝업 단추는 내용 창이 너무 많아 탭으로 적절하게 표시할 수 없는 경우 적절한 대안이 될 수 있습니다.
>




**Avoid providing more than six tabs in a tab view.** Having more than six tabs can be overwhelming and create layout issues. If you have six or more tabs, consider another way to implement your app’s user interface. For example, you may find that the tabs would be better suited as view options in a pop-up button menu.
> 탭 보기에서 6개 이상의 탭을 제공하지 마십시오. 6개 이상의 탭은 너무 많아 레이아웃 문제가 발생할 수 있습니다. 탭이 6개 이상 있는 경우 앱의 사용자 인터페이스를 구현하는 다른 방법을 고려하십시오. 예를 들어, 팝업 버튼 메뉴의 보기 옵션으로 탭이 더 적합할 수 있습니다.
>




For developer guidance, see [NSTabView](https://developer.apple.com/documentation/appkit/nstabview).

# **Anatomy**

You can position the tabbed control on any side of the content area: top, bottom, left, or right. You can also hide the controls, which is appropriate when you switch the panes programmatically.
> 상단, 하단, 왼쪽 또는 오른쪽에 탭으로 된 컨트롤을 배치할 수 있습니다. 또한 컨트롤을 숨길 수도 있습니다. 이는 창을 프로그래밍 방식으로 전환할 때 적합합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/top_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/top_2x.png)

Top tabs

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/bottom_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/bottom_2x.png)

Bottom tabs

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/left_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/left_2x.png)

Left tabs

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/right_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/right_2x.png)

Right tabs

When you hide the tabbed control, the content area can be borderless, bezeled, or bordered with a line. A borderless view can be solid or transparent.
> 탭으로 표시된 컨트롤을 숨기면 내용 영역이 테두리 없음, 베젤링 또는 선으로 테두리를 둘 수 있습니다. 테두리 없는 보기는 솔리드 또는 투명일 수 있습니다.
>




**In general, inset a tab view by leaving a margin of window-body area on all sides of a tab view.** This layout looks clean and leaves room for additional controls that aren’t directly related to the contents of the tab view. For example, the lock button in Date & Time settings is outside of the tab view because it applies to all tabs. You can extend a tab view to meet the window edges, but this layout is unusual.
> 일반적으로 탭 보기의 모든 측면에 창-본문 영역의 여백을 남겨 탭 보기를 삽입합니다. 이 레이아웃은 깔끔해 보이고 탭 보기의 내용과 직접 관련이 없는 추가 컨트롤을 위한 공간을 확보합니다. 예를 들어, 날짜 및 시간 설정의 잠금 단추는 모든 탭에 적용되므로 탭 보기 외부에 있습니다. 창 가장자리에 맞게 탭 보기를 확장할 수 있지만 이 레이아웃은 일반적이지 않습니다.
>




# **Platform considerations**

*Not supported in iOS, iPadOS, watchOS, or tvOS*
> iOS, iPadOS, watchOS 또는 tvOS에서 지원되지 않음
>




# **iOS, iPadOS**

For similar functionality, consider using a [segmented control](../components/selection-and-input/segmented-controls) instead.
> 유사한 기능을 사용하려면 세그먼트화된 컨트롤을 대신 사용하는 것이 좋습니다.
>



