# **[technologies] researchkit**

# A research app lets people everywhere participate in important medical research studies.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-ResearchKit-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-ResearchKit-intro_2x.png)

The ResearchKit framework provides predesigned screens and transitions that make it easy to design and build an engaging custom research app. For developer guidance, see [Research & Care > ResearchKit](https://www.researchandcare.org/researchkit/).

These guidelines are for informational purposes only and do not constitute legal advice. Contact an attorney to obtain advice with respect to the development of a research app and any applicable laws.

# **Creating the onboarding experience**

When opening a research app for the first time, people encounter a series of screens that introduce them to the study, determine their eligibility to participate, request permission to proceed with the study, and, when appropriate, grant access to personal data. These screens aren’t typically revisited once they’ve been completed, so clarity is essential.

**Always display the onboarding screens in the correct order.**

![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ResearchKit-Diagram_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ResearchKit-Diagram_2x.png)

### **1. Introduction**

**Provide an introduction that informs and provides a call to action.** Clearly describe the subject and purpose of your study. Also allow existing participants to quickly log in and continue an in-progress study.

![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Introduction-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Introduction-Screen_2x.png)

### **2. Determine eligibility**

**Determine eligibility as soon as possible.** People don’t need to move on to the consent section if they’re not eligible for the study. Only present eligibility requirements that are necessary for your study. Use simple, straightforward language that describes the requirements, and make it easy to enter information.

![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Eligibility-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Eligibility-Screen_2x.png)

### **3. Get informed consent**

**Make sure participants understand your study before you get their consent.** ResearchKit helps you make the consent process concise and friendly, while still allowing you to incorporate into the consent any legal requirements or requirements set by an institutional review board or ethics review board. Make sure that your app complies with the applicable App Store Guidelines, including the consent requirements. Typically, the consent section explains how the study works, ensures that participants understand the study and their responsibilities, and gets the participant’s consent.

**Break a long consent form into easily digestible sections.** Each section can cover one aspect of the study, such as data gathering, data use, potential benefits, possible risks, time commitment, how to withdraw, and so on. For each section, use simple, straightforward language to provide a high-level overview. If necessary, provide a more detailed explanation of the section that participants can read by tapping a Learn More button. Participants should be able to view the entire consent form before they agree to participate.

![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ConsentSections_Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ConsentSections_Screen_2x.png)

Play

Replay

**If it makes sense, provide a quiz that tests the participant’s understanding.** You might do this for questions the participant would otherwise be asked when obtaining consent in person.

![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ConsentQuiz-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ConsentQuiz-Screen_2x.png)

**Get the participant’s consent and, if appropriate, some contact information.** After agreeing to join the study, participants receive a confirmation dialog, which should be followed by screens in which they provide their signature and contact details. Most research apps email participants a PDF version of the consent form for their records.

![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ConsentSignature-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ConsentSignature-Screen_2x.png)

### **4. Request permission to access data**

**Get permission to access the participant’s device or data, and to send notifications.** Clearly explain why your research app needs access to location, Health, or other data, and don’t request access to data that isn’t critical to your study. If your app requires it, also ask for permission to send notifications to the participant’s device.

![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/PermissionsHealthData-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/PermissionsHealthData-Screen_2x.png)

# **Conducting research**

To get input from participants, your study might use surveys, active tasks, or a combination of both. Depending on the architecture of your study, participants may interact with each section multiple times or only once.

**Create surveys that keep participants focused and engaged.** ResearchKit provides many customizable screens you can use in your surveys, and makes it easy to present questions that require different types of answers, such as true or false, multiple choice, dates and times, sliding scales, and open-ended text entry. As you use ResearchKit screens to design a survey, follow these guidelines to provide a great experience:

- Tell participants how many questions there are and about how long the survey will take.
- Use one screen per question.
- Show participants their progress in the survey.
- Keep the survey as short as possible. Several short surveys tend to work better than one long survey.
- For questions that require some additional explanation, use the standard font for the question and a slightly smaller font for the explanatory text.
- Tell participants when the survey is complete.

![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/SurveyQuestionType1-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/SurveyQuestionType1-Screen_2x.png)

**Make active tasks easy to understand.** An active task requires the participant to engage in an activity, such as speaking into the microphone, tapping fingers on the screen, walking, or performing a memory test. Follow these guidelines to encourage participants to perform an active task and give them the best chance of success:

- Describe how to perform the task using clear, simple language.
- Explain any requirements, such as if the task must be performed at a particular time or under specific circumstances.
- Make sure participants can tell when the task is complete.

![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ActiveTasks-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/ActiveTasks-Screen_2x.png)

# **Managing personal information and providing encouragement**

ResearchKit offers a profile screen you can use to let participants manage personal information while they’re in your research app. It’s also a good idea to design a custom screen that motivates people and gives them a way to track progress in the study. Ideally, both screens should be accessible at any time in your app.

**Use a profile to help participants manage personal data related to your study.** A profile screen can let people edit data that might change during the course of the study—such as weight or sleep habits—and remind them of upcoming activities. A profile screen can also provide an easy way to leave a study and view important information, such as the consent document and privacy policy.

![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Profile-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Profile-Screen_2x.png)

**Use a dashboard to show progress and motivate participants to continue.** If appropriate for your study, use a dashboard to provide encouraging feedback, such as daily progress, weekly assessments, results from specific activities, and even results that compare the participant’s results with aggregated results from others in the study.

![https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Dashboard-Screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit/images/Dashboard-Screen_2x.png)