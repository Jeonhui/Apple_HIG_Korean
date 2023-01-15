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

