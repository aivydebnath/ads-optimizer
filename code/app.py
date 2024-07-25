import streamlit as st

# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state.page = 'start'
if 'auction_option' not in st.session_state:
    st.session_state.auction_option = None
if 'action' not in st.session_state:
    st.session_state.action = None

def show_start_page():
    if st.button('Create Campaign'):
        st.session_state.page = 'select_option'

def show_option_page():
    option = st.selectbox('Choose an option', ('Select...', 'Auction'))
    
    if option == 'Auction':
        st.session_state.page = 'auction_options'

def show_auction_options_page():
    st.write('You selected Auction. Please choose one of the following options:')
    auction_options = ['Awareness', 'Traffic', 'Engagement', 'Leads', 'App Promotion', 'Sales']
    st.session_state.auction_option = st.selectbox('Auction Options', auction_options, index=None)
    
    # Continue button is enabled only if an auction option is selected
    if st.session_state.auction_option:
        if st.button('Continue'):
            st.session_state.page = 'action_page'

def show_action_page():
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.write("**Options**")
        if st.button('New Campaign'):
            st.session_state.action = 'New Campaign'
        if st.button('New Ad Set'):
            st.session_state.action = 'New Ad Set'
        if st.button('New Ad'):
            st.session_state.action = 'New Ad'
    
    with col2:
        st.write("**Action Details**")
        if st.session_state.action == 'New Campaign':
            st.write('Click on "Create new Campaign".')
        elif st.session_state.action == 'New Ad Set':
            st.write('Click on "Create new Ad Set".')
        elif st.session_state.action == 'New Ad':
            st.write('Click on "Create new Ad".')

# Display pages based on session state
if st.session_state.page == 'start':
    show_start_page()
elif st.session_state.page == 'select_option':
    show_option_page()
elif st.session_state.page == 'auction_options':
    show_auction_options_page()
elif st.session_state.page == 'action_page':
    show_action_page()
