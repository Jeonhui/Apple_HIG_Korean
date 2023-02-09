# **[technologies] researchkit**

# A research app lets people everywhere participate in important medical research studies.
> 연구 앱은 모든 곳의 사람들이 중요한 의학 연구에 참여할 수 있게 해준다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-ResearchKit-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-ResearchKit-intro_2x.png)

The ResearchKit framework provides predesigned screens and transitions that make it easy to design and build an engaging custom research app. For developer guidance, see [Research & Care > ResearchKit](https://www.researchandcare.org/researchkit/).
> ResearchKit 프레임워크는 매력적인 맞춤형 연구 앱을 쉽게 설계하고 구축할 수 있도록 미리 설계된 화면과 전환을 제공한다. 개발자 지침은 Research & Care > Research Kit를 참조하십시오.
>




These guidelines are for informational purposes only and do not constitute legal advice. Contact an attorney to obtain advice with respect to the development of a research app and any applicable laws.
> 이 지침은 정보 제공을 위한 것일 뿐 법률 자문에 해당하지 않습니다. 변호사에게 연락하여 연구 앱 개발과 관련된 법률에 대한 조언을 구하십시오.
>




# **Creating the onboarding experience**

When opening a research app for the first time, people encounter a series of screens that introduce them to the study, determine their eligibility to participate, request permission to proceed with the study, and, when appropriate, grant access to personal data. These screens aren’t typically revisited once they’ve been completed, so clarity is essential.
> 연구 앱을 처음 열면 연구를 소개하고, 참여 자격을 결정하고, 연구 진행 허가를 요청하고, 해당 시 개인 데이터에 대한 접근 권한을 부여하는 일련의 화면을 접하게 된다. 이러한 화면은 일반적으로 완료된 후 다시 방문되지 않으므로 명확성이 필수적이다.
>




**Always display the onboarding screens in the correct order.**
> 항상 온보딩 화면을 올바른 순서로 표시하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ResearchKit-Diagram_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ResearchKit-Diagram_2x.png)

### **1. Introduction**

**Provide an introduction that informs and provides a call to action.** Clearly describe the subject and purpose of your study. Also allow existing participants to quickly log in and continue an in-progress study.
> 행동에 대한 호소를 알리고 제공하는 소개를 제공하십시오. 연구의 주제와 목적을 명확하게 설명하십시오. 또한 기존 참가자가 빠르게 로그인하고 진행 중인 스터디를 계속할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Introduction-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Introduction-Screen_2x.png)

### **2. Determine eligibility**

**Determine eligibility as soon as possible.** People don’t need to move on to the consent section if they’re not eligible for the study. Only present eligibility requirements that are necessary for your study. Use simple, straightforward language that describes the requirements, and make it easy to enter information.
> 가능한 한 빨리 자격을 결정하세요. 만약 그들이 연구에 적합하지 않다면, 사람들은 동의란으로 이동할 필요가 없습니다. 학습에 필요한 자격 요건만 제시합니다. 요구 사항을 설명하는 단순하고 간단한 언어를 사용하여 정보를 쉽게 입력할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Eligibility-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Eligibility-Screen_2x.png)

### **3. Get informed consent**

**Make sure participants understand your study before you get their consent.** ResearchKit helps you make the consent process concise and friendly, while still allowing you to incorporate into the consent any legal requirements or requirements set by an institutional review board or ethics review board. Make sure that your app complies with the applicable App Store Guidelines, including the consent requirements. Typically, the consent section explains how the study works, ensures that participants understand the study and their responsibilities, and gets the participant’s consent.
> 동의를 얻기 전에 참가자들이 여러분의 연구를 이해하고 있는지 확인하십시오. ResearchKit는 동의 과정을 간결하고 친근하게 만드는 동시에 기관 검토 위원회 또는 윤리 검토 위원회에서 정한 법적 요구 사항을 동의에 통합할 수 있도록 도와줍니다. 앱이 동의 요구 사항을 포함하여 해당 앱 스토어 지침을 준수하는지 확인하십시오. 일반적으로 동의 섹션은 연구의 작동 방식을 설명하고, 참가자가 연구와 자신의 책임을 이해하도록 보장하며, 참가자의 동의를 얻습니다.
>




**Break a long consent form into easily digestible sections.** Each section can cover one aspect of the study, such as data gathering, data use, potential benefits, possible risks, time commitment, how to withdraw, and so on. For each section, use simple, straightforward language to provide a high-level overview. If necessary, provide a more detailed explanation of the section that participants can read by tapping a Learn More button. Participants should be able to view the entire consent form before they agree to participate.
> 긴 동의서 양식을 쉽게 소화할 수 있는 섹션으로 나누십시오. 각 섹션은 데이터 수집, 데이터 사용, 잠재적 이점, 가능한 위험, 시간 약속, 철회 방법 등과 같은 연구의 한 측면을 다룰 수 있습니다. 각 섹션에 대해 단순하고 간단한 언어를 사용하여 개요를 제공합니다. 필요한 경우 참가자가 자세히 알아보기 버튼을 눌러 읽을 수 있는 섹션에 대한 자세한 설명을 제공합니다. 참가자는 참가에 동의하기 전에 전체 동의서를 볼 수 있어야 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ConsentSections_Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ConsentSections_Screen_2x.png)

Play

Replay

**If it makes sense, provide a quiz that tests the participant’s understanding.** You might do this for questions the participant would otherwise be asked when obtaining consent in person.
> 타당하다면 참가자의 이해도를 테스트하는 퀴즈를 제공하십시오. 그렇지 않으면 참가자가 직접 동의를 얻을 때 물어볼 수 있는 질문에 대해 이렇게 할 수도 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ConsentQuiz-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ConsentQuiz-Screen_2x.png)

**Get the participant’s consent and, if appropriate, some contact information.** After agreeing to join the study, participants receive a confirmation dialog, which should be followed by screens in which they provide their signature and contact details. Most research apps email participants a PDF version of the consent form for their records.
> 참가자의 동의와 해당하는 경우 일부 연락처 정보를 얻습니다. 참가자는 연구에 참여하기로 동의한 후 확인 대화상자를 받게 되며, 이 대화상자 뒤에 서명과 연락처 정보를 제공하는 화면이 표시됩니다. 대부분의 연구 앱들은 참가자들에게 PDF 버전의 동의서를 이메일로 보내 그들의 기록을 요구한다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ConsentSignature-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ConsentSignature-Screen_2x.png)

### **4. Request permission to access data**
> 4. 자료 접근 허가 요청
>




**Get permission to access the participant’s device or data, and to send notifications.** Clearly explain why your research app needs access to location, Health, or other data, and don’t request access to data that isn’t critical to your study. If your app requires it, also ask for permission to send notifications to the participant’s device.
> 참가자의 장치나 데이터에 액세스하고 알림을 보낼 수 있는 권한을 얻으십시오. 연구 응용 프로그램이 위치, 상태 또는 기타 데이터에 액세스해야 하는 이유를 명확히 설명하고, 연구에 중요하지 않은 데이터에 대한 액세스를 요청하지 마십시오. 앱에 필요한 경우 참가자의 장치로 알림을 보낼 수 있는 권한도 요청하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/PermissionsHealthData-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/PermissionsHealthData-Screen_2x.png)

# **Conducting research**

To get input from participants, your study might use surveys, active tasks, or a combination of both. Depending on the architecture of your study, participants may interact with each section multiple times or only once.
> 참가자의 의견을 얻기 위해 설문조사, 활성 작업 또는 둘을 모두 사용할 수 있습니다. 스터디의 아키텍처에 따라 참가자는 각 섹션과 여러 번 또는 한 번만 상호 작용할 수 있습니다.
>




**Create surveys that keep participants focused and engaged.** ResearchKit provides many customizable screens you can use in your surveys, and makes it easy to present questions that require different types of answers, such as true or false, multiple choice, dates and times, sliding scales, and open-ended text entry. As you use ResearchKit screens to design a survey, follow these guidelines to provide a great experience:
> 참가자가 집중하고 참여할 수 있도록 설문조사를 작성합니다. ResearchKit은 설문조사에 사용할 수 있는 많은 사용자 정의 가능한 화면을 제공하며, 참 또는 거짓, 객관식 선택, 날짜 및 시간, 슬라이드 축척, 개방형 텍스트 입력 등 다양한 유형의 답변이 필요한 질문을 쉽게 제시할 수 있도록 합니다. ResearchKit 화면을 사용하여 설문조사를 설계할 때 다음 지침에 따라 훌륭한 환경을 제공하십시오:
>




- Tell participants how many questions there are and about how long the survey will take.
- >  참가자들에게 질문이 몇 개이고 설문조사에 소요되는 시간을 알려줍니다.

- Use one screen per question.
- >  질문당 하나의 화면을 사용합니다.

- Show participants their progress in the survey.
- >  참가자들에게 설문조사 진행 상황을 보여줍니다.

- Keep the survey as short as possible. Several short surveys tend to work better than one long survey.
- >  설문조사를 가능한 짧게 유지합니다. 여러 개의 짧은 설문조사가 한 개의 긴 설문조사보다 더 효과적인 경향이 있습니다.

- For questions that require some additional explanation, use the standard font for the question and a slightly smaller font for the explanatory text.
- >  추가 설명이 필요한 질문의 경우 질문에는 표준 글꼴을 사용하고 설명 텍스트에는 약간 더 작은 글꼴을 사용합니다.

- Tell participants when the survey is complete.
- >  설문조사가 완료되면 참가자에게 말합니다.


![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/SurveyQuestionType1-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/SurveyQuestionType1-Screen_2x.png)

**Make active tasks easy to understand.** An active task requires the participant to engage in an activity, such as speaking into the microphone, tapping fingers on the screen, walking, or performing a memory test. Follow these guidelines to encourage participants to perform an active task and give them the best chance of success:
> 활동적인 작업을 이해하기 쉽게 만드십시오. 활동적인 작업은 참가자가 마이크에 대고 말하기, 화면 손가락 두드리기, 걷기 또는 기억 테스트 수행과 같은 활동에 참여해야 합니다. 참가자들이 활동적인 작업을 수행하도록 장려하고 성공의 가장 좋은 기회를 제공하기 위해 다음 지침을 따르십시오:
>




- Describe how to perform the task using clear, simple language.
- >  명확하고 간단한 언어를 사용하여 작업을 수행하는 방법을 설명합니다.

- Explain any requirements, such as if the task must be performed at a particular time or under specific circumstances.
- >  작업이 특정 시간에 수행되어야 하는지 또는 특정 상황에서 수행되어야 하는지와 같은 요구 사항을 설명합니다.

- Make sure participants can tell when the task is complete.
- >  참가자가 과제가 완료되면 알 수 있는지 확인합니다.


![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ActiveTasks-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ActiveTasks-Screen_2x.png)

# **Managing personal information and providing encouragement**
> 개인 정보 관리 및 격려 제공
>




ResearchKit offers a profile screen you can use to let participants manage personal information while they’re in your research app. It’s also a good idea to design a custom screen that motivates people and gives them a way to track progress in the study. Ideally, both screens should be accessible at any time in your app.
> ResearchKit은 참가자가 연구 앱에 있는 동안 개인 정보를 관리할 수 있도록 사용할 수 있는 프로필 화면을 제공합니다. 사람들에게 동기를 부여하고 연구 진행 상황을 추적할 수 있는 방법을 제공하는 사용자 정의 화면을 설계하는 것도 좋은 방법입니다. 이상적으로는 앱에서 언제든지 두 화면에 모두 액세스할 수 있어야 합니다.
>




**Use a profile to help participants manage personal data related to your study.** A profile screen can let people edit data that might change during the course of the study—such as weight or sleep habits—and remind them of upcoming activities. A profile screen can also provide an easy way to leave a study and view important information, such as the consent document and privacy policy.
> 프로필 화면을 사용하여 참가자가 스터디와 관련된 개인 데이터를 관리할 수 있습니다. 프로필 화면을 사용하면 체중이나 수면 습관 등 스터디 진행 중에 변경될 수 있는 데이터를 편집하고 다음 활동을 알릴 수 있습니다. 프로필 화면은 또한 스터디를 종료하고 동의 문서 및 개인 정보 보호 정책과 같은 중요한 정보를 쉽게 볼 수 있는 방법을 제공할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Profile-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Profile-Screen_2x.png)

**Use a dashboard to show progress and motivate participants to continue.** If appropriate for your study, use a dashboard to provide encouraging feedback, such as daily progress, weekly assessments, results from specific activities, and even results that compare the participant’s results with aggregated results from others in the study.
> 대시보드를 사용하여 진행 상황을 보여주고 참가자들이 계속하도록 동기를 부여합니다. 연구에 적합한 경우 대시보드를 사용하여 일일 진행 상황, 주간 평가, 특정 활동의 결과, 심지어 참가자의 결과를 다른 참가자의 집계된 결과와 비교하는 결과와 같은 고무적인 피드백을 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Dashboard-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Dashboard-Screen_2x.png)
