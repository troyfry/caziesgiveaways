import streamlit as st

# Page Configuration
st.set_page_config(page_title="Jotform Submission", page_icon="📋", layout="centered")

# App Title
st.title("Free Prompting Cheat Sheet")

# Description
st.write("""
Please use the form below to submit your details.
The form is securely hosted using Jotform.
""")

# Embed Jotform
# Replace 'your_jotform_url' with the actual Jotform embed code
jotform_embed_code = '''

    
    <iframe
      id="JotFormIFrame-250217507428151"
      title="CheatSheet- Prompting"
      onload="window.parent.scrollTo(0,0)"
      allowtransparency="true"
      allow="geolocation; microphone; camera; fullscreen"
      src="https://form.jotform.com/250217507428151"
      frameborder="0"
      style="min-width:100%;max-width:100%;height:539px;border:none;"
      scrolling="no"
    >
    </iframe>
    <script src='https://cdn.jotfor.ms/s/umd/latest/for-form-embed-handler.js'></script>
    <script>window.jotformEmbedHandler("iframe[id='JotFormIFrame-250217507428151']", "https://form.jotform.com/")</script>

</iframe>
'''

st.components.v1.html(jotform_embed_code, height=800)

# Footer
st.write("""
Cazie's AI Learning Lab. Your email is not shared!
""")
