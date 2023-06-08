# **[technologies-homekit] setup**

The Home app makes it easy for people to discover, add, name, and specify the location of accessories. Even if your accessory requires additional custom setup, you can take advantage of the system-provided setup flow.

# **Streamline the setup experience**

**Use the system-provided setup flow to give users a familiar experience.** The HomeKit setup flow works more quickly than traditional setup flows because it lets people name accessories, join networks, pair with HomeKit, assign room and service categories, and designate favorites in just a few steps. Using the system-provided setup flow also lets your app focus on promoting the custom functionality that makes your accessory unique. For developer guidance, see the [HMHome method](https://developer.apple.com/documentation/homekit/hmhome/2941039-addandsetupaccessories)for adding accessories.

**Provide context to explain why you need access to people's Home data.** Create a purpose string with a phrase that describes why you’re asking for the user’s permission to access their data, such as "Enables you to control this accessory with the Apple Home app and Siri across your Apple devices."

**Don't require people to create an account or supply personal information.** Instead, defer to HomeKit for any information you might need. If your app provides additional services that require an account, such as cloud services, make account setup optional and wait until after initial HomeKit setup to offer it.

**Honor the user’s setup choice.** When people choose to use HomeKit to set up your accessory, don’t force them to set up other platforms during the HomeKit setup flow. A cross-platform setup experience prevents people from using the accessory right away and can cause confusion by presenting too many ways to control the accessory.

**Carefully consider how and when to provide a custom accessory setup experience.** Always begin by presenting the system-provided setup flow. Then, after the accessory's basic functionality is enabled, offer a custom post-setup experience that highlights the unique features of your accessory and helps people get the most out of it. For example, a light manufacturer's app could help people create personalized light scenes in their homes using key colors scanned in from photos in their library.

# **Help people choose useful names**

**Suggest service names that suit your accessory.** If your app detects that the user has created a suboptimal name for Siri voice controls, recommend alternatives that you know will work well for most people. Never suggest company names or model numbers for use as service names.

**Check that user-provided names follow HomeKit naming rules.** If your app lets people rename services, make sure that the new names follow the rules. (The system-provided setup flow automatically checks the original names.) If people enter a name that breaks one or more rules, briefly explain the problem and suggest some alternative names that work. Here are the rules:

- Use only alphanumeric, space, and apostrophe characters.
- Start and end with an alphabetic or numeric character.
- Don't include emojis.

[제목 없음](https://www.notion.so/68e813d76fe24a30a363bc385014cf0c)

**Help people avoid creating names that include location information.** It’s natural for someone to use “kitchen light” to name a light in the kitchen, but including the room name in the service name can lead to unpredictable results when controlling the accessory by voice. Your app should detect service names that duplicate location information and help people fix them. For example, you might present a post-setup experience that removes the room or zone from a service name and encourages people to assign the accessory to that room or zone instead.