# **[technologies-carekit] views**

CareKit UI provides customizable views organized into three categories — tasks, charts, and contacts — and defines several default view styles in each. To design a CareKit app, you simply choose the view styles you need and supply CareKit Store data to display in them.
> CareKit UI는 작업, 차트 및 연락처의 세 가지 범주로 구성된 사용자 정의 가능한 보기를 제공하고 각 범주에서 몇 가지 기본 보기 스타일을 정의합니다. CareKit 앱을 설계하려면 필요한 뷰 스타일을 선택하고 해당 뷰 스타일에 표시할 CareKit Store 데이터를 제공하기만 하면 됩니다.
>




Each view category is designed to support specific types of content and interaction. To ensure a consistent experience, use each view type for its intended purpose.
> 각 보기 범주는 특정 유형의 내용 및 상호 작용을 지원하도록 설계되었습니다. 일관된 환경을 유지하려면 각 보기 유형을 원하는 용도로 사용하십시오.
>




| Category | Purpose                                                                                                                           |
|----------|-----------------------------------------------------------------------------------------------------------------------------------|
| tasks    | Present tasks, like taking medication or doing physical therapy.Enable logging of patient symptoms and other data.                |
| charts   | Display graphical data that can help people understand how their treatment is progressing.                                        |
| contacts | Display contact information.Support communication through phone, message, and email, and link to a map of the contact's location. |

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/ck-tasks-and-charts_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/ck-tasks-and-charts_2x.png)

Tasks and charts

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/ck-contacts_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/ck-contacts_2x.png)

Contacts

A CareKit UI view consists of a header and may include a stack of content subviews. Located at the top of the view, the header can display text, a symbol, and a disclosure indicator, and can include a separator at its bottom edge. The content stack appears below the header and displays your content subviews in a vertical arrangement.
> CareKit UI 보기는 헤더로 구성되며 콘텐츠 하위 보기의 스택을 포함할 수 있습니다. 보기의 맨 위에 있는 헤더는 텍스트, 기호 및 표시 표시기를 표시할 수 있으며, 하단 가장자리에 구분 기호를 포함할 수 있습니다. 내용 스택은 머리글 아래에 나타나고 내용 하위 보기를 수직 배열로 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/ck-view-components_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/ck-view-components_2x.png)

CareKit UI takes care of all the layout constraints within a view, so you don't have to worry about breaking existing constraints when you add new subviews to the stack.
> CareKit UI는 뷰 내의 모든 레이아웃 제약 조건을 처리하므로 스택에 새 하위 뷰를 추가할 때 기존 제약 조건을 깰 걱정이 없습니다.
>




# **Tasks**

A care plan generally presents a set of prescribed actions for people to perform, such as taking medication, eating specific foods, exercising, or reporting symptoms. CareKit UI defines several styles of task views you can use to display prescribed actions. Typically, you customize a task view by providing the information to display, often by specifying data stored in an on-device CareKit Store database. In some cases, you might also supply custom UI elements.
> 치료 계획은 일반적으로 약물 복용, 특정 음식 섭취, 운동 또는 증상 보고와 같은 사람들이 수행할 수 있도록 규정된 일련의 행동을 제시한다. CareKit UI는 지정된 작업을 표시하는 데 사용할 수 있는 여러 가지 작업 보기 스타일을 정의합니다. 일반적으로 표시할 정보를 제공하여 작업 보기를 사용자 정의하며, 종종 장치의 CareKit Store 데이터베이스에 저장된 데이터를 지정합니다. 경우에 따라 사용자 지정 UI 요소를 제공할 수도 있습니다.
>




A task can contain the following types of information.
> 태스크에는 다음과 같은 유형의 정보가 포함될 수 있습니다.
>




| Information | Required | Description | Example value |
| --- | --- | --- | --- |
| Title | Yes | A word or short phrase that introduces the task. | Ibuprofen |
| Schedule | Yes | The schedule on which a task must be completed. | Four times a day |
| Instructions | No | Detailed instructions, recommendations, and warnings. | Take 1 tablet every 4-6 hours (not to exceed 4 tablets daily). |
| Group ID | No | An identifier you can use to group similar tasks in ways that make sense in your app. | A category identifier like medication or exercise. |

In CareKit 2.0, CareKit UI defines five styles of task views: simple, instructions, log, checklist, and grid. Each style is designed to support a particular use case.
> CareKit 2.0에서 CareKit UI는 단순, 지침, 로그, 체크리스트 및 그리드의 다섯 가지 작업 보기 스타일을 정의합니다. 각 스타일은 특정 사용 사례를 지원하도록 설계되었습니다.
>




**Use the simple style for a one-step task.** The default simple-style view consists of a header area that contains a title, subtitle, and button. You provide the title and subtitle, and you can provide a custom image to display in the button when the task is complete. If you don't supply an image, CareKit shows that a task is complete by filling in the button and displaying a checkmark. Because the default simple-style view doesn't include a content stack, consider using a different task style if you need to display additional content.
> 한 단계 작업에 단순 스타일을 사용합니다. 기본 단순 스타일 보기는 제목, 부제 및 단추를 포함하는 머리글 영역으로 구성됩니다. 제목과 부제를 제공하고, 태스크가 완료될 때 버튼에 표시할 사용자 정의 이미지를 제공할 수 있습니다. 이미지를 제공하지 않으면 CareKit는 버튼을 채우고 확인 표시를 표시하여 작업이 완료되었음을 표시합니다. 기본 단순 스타일 보기에는 내용 스택이 없으므로, 추가 내용을 표시해야 할 경우 다른 태스크 스타일을 사용하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/simple-task_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/simple-task_2x.png)

**Use the instructions style when you need to add informative text to a simple task.** For example, if a single-step medication task should include additional information — such as "Take on an empty stomach" or "Take at bedtime" — you can use an instructions style task to display it.
> 간단한 작업에 유용한 텍스트를 추가해야 할 때는 지침 유형을 사용합니다. 예를 들어, 한 단계의 약물 작업에 "공복 시 복용" 또는 "잠잘 때 복용"과 같은 추가 정보가 포함되어야 하는 경우 지침 유형 작업을 사용하여 표시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/instructions-task_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/instructions-task_2x.png)

**Use the log style to help people log events.** For example, you could use this task style to display a button people can tap whenever they feel nauseated. The log-style task can automatically display a timestamp every time the patient logs an event.
> 로그 스타일을 사용하여 사용자가 이벤트를 기록할 수 있습니다. 예를 들어, 이 작업 스타일을 사용하여 사용자가 메스꺼움을 느낄 때마다 누를 수 있는 단추를 표시할 수 있습니다. 로그 스타일 작업은 환자가 이벤트를 기록할 때마다 타임스탬프를 자동으로 표시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/log-task_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/log-task_2x.png)

**Use the checklist style to display a list of actions or steps in a multistep task.** For example, if people should take a medication three times per day, you could display the three scheduled times in a checklist. Each checklist item can include a text description and a button that people can tap to mark the item as done. By default, a checklist task can also display instructional text below the list.
> 체크리스트 스타일을 사용하여 다단계 작업의 작업 또는 단계 목록을 표시합니다. 예를 들어, 사람들이 하루에 세 번 약을 복용해야 하는 경우, 예약된 세 시간을 체크리스트에 표시할 수 있습니다. 각 체크리스트 항목에는 텍스트 설명과 버튼을 눌러 항목을 완료로 표시할 수 있습니다. 기본적으로 체크리스트 태스크는 목록 아래에 지시문을 표시할 수도 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/checklist-task_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/checklist-task_2x.png)

**Use the grid style to display a grid of buttons in a multistep task.** Like the checklist style, the grid style also supports a multistep task, but it displays the steps in a more compact arrangement. You can supply a succinct title for each button (if you need to provide additional description for each button, you might want to use the checklist style instead). By default, a grid-style task can also display instructional text below the grid of buttons. Unlike other task styles, the grid style gives you access to its underlying collection view, which means that you can display custom UI elements in the grid layout.
> 그리드 스타일을 사용하여 다단계 작업의 버튼 그리드를 표시할 수 있습니다. 체크리스트 스타일과 마찬가지로 그리드 스타일도 다단계 작업을 지원하지만 단계를 보다 간결하게 표시할 수 있습니다. 각 단추에 대한 간략한 제목을 제공할 수 있습니다(각 단추에 대한 추가 설명을 제공해야 하는 경우 대신 체크리스트 스타일을 사용할 수 있습니다). 기본적으로 그리드 스타일 작업은 단추 그리드 아래에 지시문을 표시할 수도 있습니다. 다른 작업 스타일과 달리 그리드 스타일을 사용하면 기본 컬렉션 보기에 액세스할 수 있으므로 그리드 레이아웃에 사용자 정의 UI 요소를 표시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/grid-task_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/grid-task_2x.png)

**Consider using color to reinforce the meaning of task items.** Color can be a good way to help people understand information at a glance. For example, you could use one color for medications and a different color for physical activities. Always avoid using color as the only way to convey information. For guidance, see [Color](../foundations/color).
> 색을 사용하여 작업 항목의 의미를 강화하는 것을 고려하십시오. 색은 사람들이 정보를 한 눈에 이해하는 데 도움이 되는 좋은 방법이 될 수 있습니다. 예를 들어, 약물에는 한 가지 색을 사용하고 신체 활동에는 다른 색을 사용할 수 있습니다. 정보를 전달하는 유일한 방법으로 색상을 사용하는 것을 항상 피하세요. 자세한 내용은 색상을 참조하십시오.
>




**Combine accuracy with simplicity when describing a task and its steps.** For example, use a medication's marketing name instead of its chemical description. Also, when the context of a task helps to clarify meaning, minimize the number of words you use. For example, a daily medication task generally tells people when to take specific medications, so it may be unnecessary to repeat words like "take."
> 작업과 단계를 설명할 때 정확성과 단순성을 결합하십시오. 예를 들어, 화학적 설명 대신 의약품의 마케팅 이름을 사용하십시오. 또한, 업무의 맥락이 의미를 명확히 하는 데 도움이 될 때, 사용하는 단어의 수를 최소화하세요. 예를 들어, 일상적인 약물 작업은 일반적으로 사람들에게 언제 특정 약물을 복용해야 하는지를 알려주기 때문에 "복용"과 같은 단어를 반복할 필요가 없을 수 있다
>




**Consider supplementing multistep or complex tasks with videos or images.** Visually demonstrating how to perform a task can help people avoid mistakes.
> 다단계 또는 복잡한 작업을 비디오 또는 이미지로 보완하는 것을 고려한다. 작업을 수행하는 방법을 시각적으로 보여주는 것은 사람들이 실수를 피하는 데 도움이 될 수 있다.
>




# **Charts**

Chart views let you present data and trends in graphical ways that can help people visualize their progress in a care plan. CareKit chart views can display both current and historical data, and update automatically with new data.
> 차트 보기를 사용하면 사람들이 진료 계획의 진행 상황을 시각화하는 데 도움이 되는 데이터와 추세를 그래픽으로 표시할 수 있습니다. CareKit 차트 보기는 현재 데이터와 과거 데이터를 모두 표시하고 새 데이터로 자동 업데이트할 수 있습니다.
>




In CareKit 2.0, CareKit UI provides three chart styles: bar, scatter, and line. For each style, you provide a descriptive title and subtitle, supply axis markers — like days of the week — and specify the data set.
> CareKit 2.0에서 CareKit UI는 막대, 산포, 선의 세 가지 차트 스타일을 제공합니다. 각 스타일에 대해 설명하는 제목과 부제를 제공하고 요일과 같은 축 마커를 제공하고 데이터 세트를 지정합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/bar-chart_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/bar-chart_2x.png)

Bar chart

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/scatter-chart_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/scatter-chart_2x.png)

Scatter chart

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/line-chart_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/line-chart_2x.png)

Line chart

**Consider highlighting narratives and trends to illustrate progress.** For example, your app could display a bar chart that shows a correlation between the number of times people took medication and their level of pain. Displaying such data can encourage better adherence to a care plan.
> 예를 들어, 앱에서 사람들이 약물을 복용한 횟수와 통증 수준 간의 상관 관계를 보여주는 막대 차트를 표시할 수 있습니다. 이러한 데이터를 표시하면 관리 계획을 더 잘 준수할 수 있다.
>




**Label chart elements clearly and succinctly.** Long, detailed labels can make a chart difficult to read and understand. Keep labels short and avoid repeating the same information. For example, a heart rate chart might use the term *BPM* in an axis label instead of using it in the label of every data point.
> 차트 요소에 명확하고 간결하게 레이블을 지정합니다. 길고 자세한 레이블은 차트를 읽고 이해하기 어려울 수 있습니다. 레이블을 짧게 유지하고 동일한 정보가 반복되지 않도록 합니다. 예를 들어, 심박수 차트는 모든 데이터 점의 레이블에서 사용하는 대신 축 레이블에서 BPM이라는 용어를 사용할 수 있습니다.
>




**Use distinct colors.** In general, avoid using different shades of the same color to mean different things. Also ensure that you use colors with sufficient contrast. For related guidance, see [Color and effects](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility#color-and-effects).
> 다른 색을 사용하세요. 일반적으로, 다른 것을 의미하기 위해 같은 색의 다른 음영을 사용하는 것을 피하세요. 또한 충분한 대비가 있는 색상을 사용해야 합니다. 관련 지침은 색상 및 효과를 참조하십시오.
>




**Consider providing a legend to add clarity.** If the colors you use to represent different types of data aren't immediately clear, include a legend that clearly and succinctly describes them.
> 다른 유형의 데이터를 나타내는 데 사용하는 색상이 명확하지 않은 경우에는 명확하고 간결하게 설명하는 범례를 포함하십시오.
>




**Clearly denote units of time.** People should immediately know whether time-based data is represented in seconds, minutes, hours, days, weeks, months, or years. If you don’t want to include this information in individual data value labels, include it in an axis label or elsewhere on the chart.
> 시간 단위를 명확하게 나타낸다. 사람들은 시간 기반 데이터가 초, 분, 시간, 일, 주, 월 또는 년으로 표시되는지 즉시 알아야 한다. 이 정보를 개별 데이터 값 레이블에 포함하지 않으려면 축 레이블이나 차트의 다른 위치에 포함하십시오.
>




**Consolidate large data sets for greater readability.** A large amount of data can make a chart unreadable by reducing the size of individual data points and presenting too much visible information. Look for ways to group and organize data for clarity and simplicity.
> 큰 데이터 세트를 통합하여 읽기 쉬움을 높입니다. 많은 양의 데이터는 개별 데이터 포인트의 크기를 줄이고 표시되는 정보를 너무 많이 표시하여 차트를 읽을 수 없게 만들 수 있습니다. 명확성과 단순성을 위해 데이터를 그룹화하고 구성하는 방법을 찾습니다.
>




**If necessary, offset data to keep charts proportional.** It’s easy for very small data points to get lost or become unreadable in a chart that also contains very large data points. If the difference between data points is significant, find ways to offset or restructure the data so all data points are readable.
> 필요한 경우 차트에 비례하도록 데이터를 오프셋합니다. 매우 작은 데이터 포인트가 손실되거나 매우 큰 데이터 포인트가 포함된 차트에서 읽을 수 없게 되기 쉽습니다. 데이터 점 간의 차이가 큰 경우 모든 데이터 점을 읽을 수 있도록 데이터를 간격띄우기하거나 재구성하는 방법을 찾습니다.
>




For developer guidance, see [CareKit > Chart Interfaces](https://developer.apple.com/documentation/carekit/chart_interfaces). To learn about ResearchKit charts, see the [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit).
> 개발자 지침은 CareKit > 차트 인터페이스를 참조하십시오. ResearchKit 차트에 대한 자세한 내용은 ResearchKit GitHub 프로젝트를 참조하십시오.
>




# **Contacts**

A care plan typically includes a care team and other trusted individuals who can help patients follow the plan. CareKit UI defines a contact view you can use to help patients communicate with the people in their care plan.
> 진료 계획에는 일반적으로 환자가 계획을 따르도록 도울 수 있는 진료 팀과 기타 신뢰할 수 있는 개인이 포함된다. CareKit UI는 환자가 진료 계획에 있는 사람과 의사소통하는 데 사용할 수 있는 연락처 보기를 정의합니다.
>




In CareKit 2.0, CareKit UI provides two styles of the contact view: simple and detailed.
> 케어킷 2.0에서 케어킷 UI는 두 가지 스타일의 접촉 뷰를 제공한다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/simple-contact_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/simple-contact_2x.png)

Simple

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/detailed-contact_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/detailed-contact_2x.png)

Detailed

**Consider using color to categorize care team members.** Color can help people identify care team members at a glance.
> 색상을 사용하여 진료팀 구성원을 분류하는 것을 고려하십시오. 색상은 사람들이 진료팀 구성원을 한 눈에 식별하는 데 도움이 될 수 있습니다.
>



