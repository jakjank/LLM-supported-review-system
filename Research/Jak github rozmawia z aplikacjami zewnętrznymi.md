**GitHub Apps and OAuth apps**
------------------------------

[https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps) 

"**Common use cases for GitHub Apps include:**

*   Automating tasks or background processes
*   Supporting "Sign in with GitHub," which allows users to sign in with their GitHub account to provide their identity in your ecosystem
*   As a developer tool, allowing users to work with GitHub by signing into your GitHub App, which can then act on their behalf
*   **Integrating your tool or external service with GitHub**"

**Z docsów GitHuba**

"In general, **GitHub Apps are preferred over OAuth apps**. GitHub Apps use fine-grained permissions, give the user more control over which repositories the app can access, and use short-lived tokens. These properties can **harden the security of your app** by limiting the damage that could be done if your app's credentials were leaked.

Similar to OAuth apps, GitHub Apps can still use OAuth 2.0 and generate a type of OAuth token (called a user access token) and take actions on behalf of a user. However, **GitHub Apps can also act independently of a user**. This is beneficial for automations that do not require user input. The app will continue to work even if the person who installed the app on an organization leaves the organization."

“There is one case where an OAuth app is preferred over a GitHub App. If your app needs to access enterprise-level resources such as the enterprise object itself, you should use an OAuth app because a **GitHub App cannot yet be given permissions against an enterprise**. GitHub Apps can still access enterprise-owned organization and repository resources.”

* * *

**Rodzaje GitHub Apps**
-----------------------

[https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps) 

**“On their own behalf”**

Jeśli chcemy, by aplikacja działała “jako ona” a nie “jako konkretny użytkownik”.

"Some examples of automations you could create with a GitHub App, where the app acts on its own behalf, include:

*   A GitHub App that uses webhooks to react to an event given a certain set of criteria. For example, you could create an automation around the REST API endpoints for reviewing requests for fine-grained personal access token that approves a request given a certain policy.
*   A GitHub App that helps repository contributors. For example, the app could post helpful resources after a contributor creates a pull request or makes a comment.
*   A GitHub App that generates short-lived tokens to give to other CI/CD tools, or to pull information from a repository."

**Responds to webhooks**

“If you want your app to respond to events on GitHub, your app should subscribe to webhooks. For example, you may want your app to leave a comment when a pull request is opened.”

**Zdefiniowane z góry akcje**

When you set up your GitHub App, you can select specific permissions for the app. These permissions determine what the app can do via the GitHub API, what they can do on behalf of a signed in user, and what webhooks the app can receive.

* * *

**Creating Github Apps**
------------------------

[https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps) 

1.  Zarejestruj GitHub App  
    [https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app)   
     
2.  Napisz kod GitHub App  
    [https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/about-writing-code-for-a-github-app](https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/about-writing-code-for-a-github-app)   
    (więcej o tym niżej)  
     
3.  Skonfiguruj autentyfikację Github App  
    [https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/about-authentication-with-a-github-app](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/about-authentication-with-a-github-app)   
     
4.  “Once you have written the code for your GitHub App, your app needs to run somewhere. If your app is a website or web app, you might host your app on a server like Azure App Service. **If your app is a client-side app, it might run on a user's device**.”  
     
5.  Zainstaluj gotową GitHub App  
    “In order to use your GitHub App, you must install the app on your organization or personal account. If your GitHub App is private, you can only install the GitHub App on the account that owns the app. **If your GitHub App is public, other users and organizations can install your app.**”  
    [https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app](https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app)   
     
6.  Opublikuj GitHub App
    1.  Ustaw jako **public.**
    2.  Opublikuj na GitHub Marketplace  
        [https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/about-github-marketplace-for-apps](https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/about-github-marketplace-for-apps)   
        lub  
        pozwalaj tylko na instalację przez link.  
        [https://docs.github.com/en/apps/sharing-github-apps/sharing-your-github-app](https://docs.github.com/en/apps/sharing-github-apps/sharing-your-github-app)   
         

* * *

**Writing Code for GitHub App that responds to webhook events**
---------------------------------------------------------------

[https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/building-a-github-app-that-responds-to-webhook-events](https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/building-a-github-app-that-responds-to-webhook-events) 

"During development, you will likely use your personal computer or codespace to run your GitHub App. You may need to make some modifications to your GitHub App registration during development.

If your app receives webhooks, you may want to use a **webhook proxy URL** to forward webhooks from GitHub to your computer or codespace. You will need to update the "Webhook URL" setting in your GitHub App registration to use your webhook proxy URL. For an example, see "Building a GitHub App that responds to webhook events."

**Instrukcja krok po kroku dla przykładowego programu w JavaScript:**  
[https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/building-a-github-app-that-responds-to-webhook-events](https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/building-a-github-app-that-responds-to-webhook-events) 

**Konfigurowanie webhook serwera:**  
[https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps) 

* * *

**Może na później?**
--------------------

[https://devopslearning.medium.com/day-13-101-days-of-devops-github-api-using-python-and-pygithub-module-c1bcbaaeada7](https://devopslearning.medium.com/day-13-101-days-of-devops-github-api-using-python-and-pygithub-module-c1bcbaaeada7) 

To wygląda jak coś, co może nam pomóc zrozumieć, **jak Python rozmawia z GitHubem.**