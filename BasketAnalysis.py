import streamlit as st
import pandas as pd
import helper as helper

customized_button = st.markdown("""
    <style >
    .stDownloadButton, div.stButton {text-align:center}
    .stDownloadButton button, div.stButton > button:first-child {
        font-weight: bold;
        background-color: #e1ecf4;
        border-radius: 3px;
        border: 1px solid #7aa7c7;
        box-shadow: rgba(255, 255, 255, .7) 0 1px 0 0 inset;
        box-sizing: border-box;
        color: #39739d !important;
        cursor: pointer;
        display: inline-block;
        line-height: 1.15385;
        margin: 0;
        outline: none;
        padding: 8px .8em;
        position: relative;
        text-align: center;
        text-decoration: none !important;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
        vertical-align: baseline;
        white-space: nowrap;
    }
}

.stDownloadButton:focus {
  box-shadow: 0 0 0 4px rgba(0, 149, 255, .15);
} 0 4px rgba(0, 149, 255, .15);
}
        }
    </style>""", unsafe_allow_html=True)

button_style = '''
<style>
    .button-8 {
        font-weight: bold;
        background-color: #e1ecf4;
        border-radius: 3px;
        border: 1px solid #7aa7c7;
        box-shadow: rgba(255, 255, 255, .7) 0 1px 0 0 inset;
        box-sizing: border-box;
        color: #39739d !important;
        cursor: pointer;
        display: inline-block;
        line-height: 1.15385;
        margin: 0;
        outline: none;
        padding: 8px .8em;
        position: relative;
        text-align: center;
        text-decoration: none !important;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
        vertical-align: baseline;
        white-space: nowrap;
}

.button-8:hover,
.button-8:focus {
  background-color: #b3d3ea;
  color: #2c5777;
}

.button-8:focus {
  box-shadow: 0 0 0 4px rgba(0, 149, 255, .15);
}

.button-8:active {
  background-color: #a0c7e4;
  box-shadow: none;
  color: #2c5777;
}
</style>

'''

def load_text(file_path):
    """A convenience function for reading in the files used for the site's text"""
    with open(file_path) as in_file:
        return in_file.read()

st.markdown('''<div style="text-align: center;">
  <h1 style="display: inline-block; text-align: center;">Basket Analysis</h1>
  <h3 style="display: inline-block;">&nbsp 🛒 🎯</h3>
</div>''', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;padding-top:0px'>How Association Rules Can Boost Your Business</h3>", unsafe_allow_html=True)


# Display the combined HTML code in Streamlit
component_profile = load_text('profile.html')
st.components.v1.html(component_profile,  height=50)


st.markdown("<p style='text-align: center'>If we find that customers who buy bread are likely to buy milk, we can create an association rule that says</p>", unsafe_allow_html=True)
st.markdown('''
<h4 style='text-align: center;font-weight: bold;'>"If a customer buys bread, they are likely to buy milk." <br><br> 🧍🏻🍞 &nbsp 🔜  &nbsp 🥛</h4>

''', unsafe_allow_html=True)
st.markdown('''
<style>
        .highlight {
            background: linear-gradient(to bottom, transparent 50%, #ADD8E6 50%);
            font-weight: bold;
        }
</style>
<p style='text-align: center'>This rule can then be used to suggest
<span class='highlight'> complementary products</span> or to create <span class='highlight'> targeted marketing campaigns</span>.</p>
''', unsafe_allow_html=True)

st.markdown(button_style + '''
<div style='text-align:center;'>
<a class='button-8' href='#association-rules-in-action'>Jump to Demo 🚀</a>
</div>

''', unsafe_allow_html=True)

st.header('Introduction to Association Rules')
st.markdown('''
<style>
        .highlight {
            background: linear-gradient(to bottom, transparent 50%, #ADD8E6 50%);
            font-weight: bold;
        }
</style>
<ul>
<li> <span style='font-weight: bold;'>Retail</span> -> Identify which products are frequently purchased together.</li>
<li> <span style='font-weight: bold;'>E-commerce </span> -> Increase sales by suggesting relevant products that the customer is likely to be interested in.</li>
<li> <span style='font-weight: bold;'>Grocery stores</span> -> If chips and salsa are frequently purchased together, they can be placed next to each other to increase sales.</li>
<li> <span style='font-weight: bold;'>Hospitality</span> -> Menu items are commonly purchased together and create meal bundles or promotional packages that include these items.</li>
</ul>
<p>As you see, Association Rules are a data mining technique used to <span class='highlight'> discover relationships </span> such as <span class='highlight'> co-occurrence </span> among items that we are interested.</p>
<p>Basket Analysis uses Association Rules to uncover relationships between items in <span class='highlight'>a transactional dataset</span> and create a set of rules.</p>
<p style='font-weight: bold;'>Rule</p>
<p>1) The antecedent: a set of items that is present in the transaction <br> 2) the consequent: a set of items that are likely to be purchased if the antecedent is present</p>
''',
unsafe_allow_html=True)

st.header('How Association Rules Work')
st.markdown('''
<style>
        .highlight {
            background: linear-gradient(to bottom, transparent 50%, #ADD8E6 50%);
            font-weight: bold;
        }
        .bold {
            font-weight: bold;
        }
</style>
<p>When two or more items are often seen or bought together it’s called <span class='highlight'> a frequency set</span>.</p>
<p>Suppose you have a clothing store.
<p>Here are some examples of transaction history from your POS.</p>
<ul>
<li>{jacket, t-shirt, jeans, shoes}</li>
<li>{dress, shoes}</li>
<li>{jacket, scarf}</li>
<li>{t-shirt, sunglasses, hat}</li>
<li>{dress, jacket, shoes}</li>
<li>{jeans, jacket, shoes}</li>
</ul>
<p> Let's say we want to use basket analysis to find out <span class='highlight'>which items are commonly bought together</span>, and use that information to make recommendations to customers.</p>
<p>To start, we can look at the itemset <span class='bold'>{jacket, shoes}</span> (if someone buy a jacket, woul you recommend shoes to them ?) </p>
<p>We can calculate the <sapn class='highlight'>confidence</sapn> of the rule "if someone buys a jacket, they are likely to buy shoes" as <span class='bold'>3/4</span>, because jacket is present in four transactions, and in three of those transactions, shoes is also present.</p>
<p>Similarly, we can look at the itemset <span class='bold'>{dress, shoes}</span>. If someone buys a dress, they are likely to buy shoes as <span class='bold'>2/2</span>, because dress is present in two transactions, and in both of those transactions, shoes is also present.</p>
<p class='bold'>Two important measures used in association rules are support and confidence.</p>
<ul>
<li>
    <span class='bold'>Support</span> measures the popularity of an itemset in the dataset.
     <ul>
      <li>If we have a dataset of 100 transactions, and the itemset {jacket, scarf} appears in 20 transactions, then the support of {jacket, scarf} is 20/100 or 0.2.</li>
    </ul>
</li>
<li>
    <span class='bold'>Confidence</span> is a measure of the strength of association between two items.
     <ul>
      <li>If we have a rule {t-shirt} -> {jeans} with 30 transactions containing t-shirt and jeans, and 50 transactions containing t-shirt, then the confidence of the rule is 30/50 or 0.6.</li>
    </ul>
</li>
</ul>
<p>In general, a high support and high confidence indicate a strong association between the items in the itemset or rule. These measures are used to identify frequent itemsets and strong association rules in a dataset.</p>
''',
unsafe_allow_html=True)

st.header('Association Rules in Action 🚀')

# Set default file path and name
DEFAULT_FILE = "Groceries_dataset.csv"

# Create a function to load the data
def load_data(file):
    df = pd.read_csv(file)
    return df

use_custom_file = st.checkbox("Use your csv file")

data = None
if use_custom_file:
    file = st.file_uploader("Upload CSV file", type=["csv"])
    st.markdown('''
    <style>
        .highlight {
            background: linear-gradient(to bottom, transparent 50%, #fce041 50%);
            font-weight: bold;
        }
        .bold {
            font-weight: bold;
        }
    </style>
    <span class='highlight'>
    The file format should be same as the demo file where each row represents one item that was purchased by a particular user at a specific date
    </span>
    <ul>
        <li>1st column = Member Number</li>
        <li>2nd column = Date of purchase</li>
        <li>3rd column = Purchased item</li>
    </ul>
    ''', unsafe_allow_html=True)
    if file is not None:
        data = load_data(file)
else:
    data = load_data(DEFAULT_FILE)

if data is not None:
    st.dataframe(data.sort_values(by=['Member_number', 'Date']))


if "clicked" not in st.session_state:
    st.session_state.clicked = False

clicked  = st.button("👉🏻  Click to generate association rules  👈🏻")
if clicked or st.session_state.get("clicked", False):
    st.session_state.clicked = True

    if st.session_state.get("builder", False):
        builder_dict = st.session_state.get('builder', {})
        builder = pd.DataFrame.from_dict(builder_dict)
        options = set(builder['source'])
        selected_option = st.selectbox("Click below to choose an item 👇🏻", options)
        st.write(builder[builder['source'] == selected_option].sort_values('confidence', ascending=False)[:5])
        top_items = builder[builder['source'] == selected_option].sort_values('confidence', ascending=False)['target'][:5]
        st.write(f'Top 5 frequently purchased together with {selected_option} 🔝: {", ".join(top_items)}')
    else:
        transactions = helper.generate_transactions(data)
        builder = helper.calculate_support_confidence(transactions)
        builder = pd.DataFrame(builder, columns=['source', 'target', 'confidence', 'support'])

        options = set(builder['source'])
        selected_option = st.selectbox("Click below to choose an item 👇🏻", options)
        st.write(builder[builder['source'] == selected_option].sort_values('confidence', ascending=False)[:5])
        top_items = builder[builder['source'] == selected_option].sort_values('confidence', ascending=False)['target'][:5]
        st.write(f'Top 5 frequently purchased together with {selected_option} 🔝: {", ".join(top_items)}')
        st.session_state.builder = builder.to_dict()
