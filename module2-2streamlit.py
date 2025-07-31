from Bio import Blast
import streamlit as st

st.title('Module 2-2')

Blast.email = st.text_input('provide your jhu email')

uploaded_file = st.file_uploader("", type='fasta')

if uploaded_file is not None:
    st.success("FASTA file uploaded")
else:
    st.info("Please upload your target FASTA file")

if st.button('run blast'):
    target_nt_fasta = uploaded_file.read()
    with st.empty():
        st.write('blast running...')
        result_stream = Blast.qblast('blastx', 'nr', target_nt_fasta)
        st.write('blast finished!')

    with open('myblast.xml', 'wb') as out_stream:
        out_stream.write(result_stream.read())
    result_stream.close()
    result_stream = open('myblast.xml', 'rb')
    blast_record = Blast.read(result_stream)

    hit = blast_record[0]
    alignment = hit[0]
    st.code(hit)
    num = 1

    for i in blast_record[:10]:
        st.write("HIT" + str(num))
        st.write(i[0])
        num = num +1
