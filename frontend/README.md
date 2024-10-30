## Frontend Coding Challenge: Exchange Listing Table with SSR

### Background:

Your task is to create a Next.js application that displays cryptocurrency exchange data fetched from a public API in a paginated table. The data should be server-side rendered (SSR).


### Requirements:

1. **Setup**:
    - Create a new project using Next.js.
    - Use any CSS-in-JS solution or CSS framework of your choice for styling. Bonus points for styled components.

2. **API Integration**:
    - Integrate with the provided API endpoint: `https://api.coingecko.com/api/v3/exchanges`.
    - Fetch and display the data in SSR mode.
    - Paginate through results. 

3. **Table Display**:
    - Display the data in a table format on the index page.
    - The table should have the following 6 columns:
        1. Exchange name with image.
        2. Year established.
        3. Country.
        4. Trust score.
        5. 24h trade volume in BTC.
        6. Normalized 24h trade volume in BTC.
    - Implement server-side pagination controls for the table. Each page should display 15 exchanges.

4. **Row Interaction**:
    - Clicking on a row should open the exchange's URL in a new browser tab.

5. **Routing**:
    - Use Next.js to set up proper routing for paginated data.
    - For example, `/page/2` should show the next set of 15 exchanges. You could also use url params, e.g. `?page=2`. Up to you.

6. **Error Handling**:
    - Gracefully handle any errors when fetching data from the API, displaying an appropriate message to the user.

7. **Styling**:
    - Ensure that the table is neatly styled, ensuring readability.
    - Add responsiveness so that the table is viewable on mobile devices.
    - Feel free to use Rated's color palette as described [here](https://docs.rated.network/brand-resources/rated-brand-guidelines#powered-by-rated-badge)
    - Feel free to also copy general styling from Rated's website.

8. **Testing**:
    - Bonus points for adding tests using Jest or similar.

### Evaluation Criteria:

1. **Functionality**: Ensure that all requirements are implemented and work as expected.
2. **Code Quality**: Clean, readable, and maintainable code.
3. **Next.js Implementation**: Proper use of server-side rendering and routing.

### Submission:

Provide a link to the GitHub repository containing your code. Include any instructions needed to run and test your application locally. Bonus points if you deploy the app to a platform like Vercel and provide the live link.

**Good luck!**