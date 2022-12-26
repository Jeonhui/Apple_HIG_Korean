# **[technologies-carekit] views**

CareKit UI provides customizable views organized into three categories — tasks, charts, and contacts — and defines several default view styles in each. To design a CareKit app, you simply choose the view styles you need and supply CareKit Store data to display in them.

Each view category is designed to support specific types of content and interaction. To ensure a consistent experience, use each view type for its intended purpose.

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

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/ck-view-components_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/ck-view-components_2x.png)

CareKit UI takes care of all the layout constraints within a view, so you don't have to worry about breaking existing constraints when you add new subviews to the stack.

# **Tasks**

A care plan generally presents a set of prescribed actions for people to perform, such as taking medication, eating specific foods, exercising, or reporting symptoms. CareKit UI defines several styles of task views you can use to display prescribed actions. Typically, you customize a task view by providing the information to display, often by specifying data stored in an on-device CareKit Store database. In some cases, you might also supply custom UI elements.

A task can contain the following types of information.

| Information | Required | Description | Example value |
| --- | --- | --- | --- |
| Title | Yes | A word or short phrase that introduces the task. | Ibuprofen |
| Schedule | Yes | The schedule on which a task must be completed. | Four times a day |
| Instructions | No | Detailed instructions, recommendations, and warnings. | Take 1 tablet every 4-6 hours (not to exceed 4 tablets daily). |
| Group ID | No | An identifier you can use to group similar tasks in ways that make sense in your app. | A category identifier like medication or exercise. |

In CareKit 2.0, CareKit UI defines five styles of task views: simple, instructions, log, checklist, and grid. Each style is designed to support a particular use case.

**Use the simple style for a one-step task.** The default simple-style view consists of a header area that contains a title, subtitle, and button. You provide the title and subtitle, and you can provide a custom image to display in the button when the task is complete. If you don't supply an image, CareKit shows that a task is complete by filling in the button and displaying a checkmark. Because the default simple-style view doesn't include a content stack, consider using a different task style if you need to display additional content.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/simple-task_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/simple-task_2x.png)

**Use the instructions style when you need to add informative text to a simple task.** For example, if a single-step medication task should include additional information — such as "Take on an empty stomach" or "Take at bedtime" — you can use an instructions style task to display it.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/instructions-task_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/instructions-task_2x.png)

**Use the log style to help people log events.** For example, you could use this task style to display a button people can tap whenever they feel nauseated. The log-style task can automatically display a timestamp every time the patient logs an event.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/log-task_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/log-task_2x.png)

**Use the checklist style to display a list of actions or steps in a multistep task.** For example, if people should take a medication three times per day, you could display the three scheduled times in a checklist. Each checklist item can include a text description and a button that people can tap to mark the item as done. By default, a checklist task can also display instructional text below the list.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/checklist-task_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/checklist-task_2x.png)

**Use the grid style to display a grid of buttons in a multistep task.** Like the checklist style, the grid style also supports a multistep task, but it displays the steps in a more compact arrangement. You can supply a succinct title for each button (if you need to provide additional description for each button, you might want to use the checklist style instead). By default, a grid-style task can also display instructional text below the grid of buttons. Unlike other task styles, the grid style gives you access to its underlying collection view, which means that you can display custom UI elements in the grid layout.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/grid-task_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/grid-task_2x.png)

**Consider using color to reinforce the meaning of task items.** Color can be a good way to help people understand information at a glance. For example, you could use one color for medications and a different color for physical activities. Always avoid using color as the only way to convey information. For guidance, see [Color](https://developer.apple.com/design/human-interface-guidelines/foundations/color).

**Combine accuracy with simplicity when describing a task and its steps.** For example, use a medication's marketing name instead of its chemical description. Also, when the context of a task helps to clarify meaning, minimize the number of words you use. For example, a daily medication task generally tells people when to take specific medications, so it may be unnecessary to repeat words like "take."

**Consider supplementing multistep or complex tasks with videos or images.** Visually demonstrating how to perform a task can help people avoid mistakes.

# **Charts**

Chart views let you present data and trends in graphical ways that can help people visualize their progress in a care plan. CareKit chart views can display both current and historical data, and update automatically with new data.

In CareKit 2.0, CareKit UI provides three chart styles: bar, scatter, and line. For each style, you provide a descriptive title and subtitle, supply axis markers — like days of the week — and specify the data set.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/bar-chart_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/bar-chart_2x.png)

Bar chart

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/scatter-chart_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/scatter-chart_2x.png)

Scatter chart

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/line-chart_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/line-chart_2x.png)

Line chart

**Consider highlighting narratives and trends to illustrate progress.** For example, your app could display a bar chart that shows a correlation between the number of times people took medication and their level of pain. Displaying such data can encourage better adherence to a care plan.

**Label chart elements clearly and succinctly.** Long, detailed labels can make a chart difficult to read and understand. Keep labels short and avoid repeating the same information. For example, a heart rate chart might use the term *BPM* in an axis label instead of using it in the label of every data point.

**Use distinct colors.** In general, avoid using different shades of the same color to mean different things. Also ensure that you use colors with sufficient contrast. For related guidance, see [Color and effects](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility#color-and-effects).

**Consider providing a legend to add clarity.** If the colors you use to represent different types of data aren't immediately clear, include a legend that clearly and succinctly describes them.

**Clearly denote units of time.** People should immediately know whether time-based data is represented in seconds, minutes, hours, days, weeks, months, or years. If you don’t want to include this information in individual data value labels, include it in an axis label or elsewhere on the chart.

**Consolidate large data sets for greater readability.** A large amount of data can make a chart unreadable by reducing the size of individual data points and presenting too much visible information. Look for ways to group and organize data for clarity and simplicity.

**If necessary, offset data to keep charts proportional.** It’s easy for very small data points to get lost or become unreadable in a chart that also contains very large data points. If the difference between data points is significant, find ways to offset or restructure the data so all data points are readable.

For developer guidance, see [CareKit > Chart Interfaces](https://developer.apple.com/documentation/carekit/chart_interfaces). To learn about ResearchKit charts, see the [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit).

# **Contacts**

A care plan typically includes a care team and other trusted individuals who can help patients follow the plan. CareKit UI defines a contact view you can use to help patients communicate with the people in their care plan.

In CareKit 2.0, CareKit UI provides two styles of the contact view: simple and detailed.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/simple-contact_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/simple-contact_2x.png)

Simple

![https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/detailed-contact_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carekit/images/detailed-contact_2x.png)

Detailed

**Consider using color to categorize care team members.** Color can help people identify care team members at a glance.