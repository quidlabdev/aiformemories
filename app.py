# Core pkgs
import streamlit as st
import numpy as np
from PIL import Image
import cv2
import requests
import time


#matplotlib.use("Agg")
st.set_option('deprecation.showfileUploaderEncoding', False)  # Apagar warnings

st.set_page_config(
	page_title="Deoldify",
	page_icon="random",
	layout="centered",
	initial_sidebar_state="expanded",
	)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



def main():
	"""Inteligencia Artificial"""
	image =  Image.open('logo.png')

	st.title("Rejuvenecedor de recuerdos")
	#st.text("Fotos")

	activites = ["Seleccione", "Subir archivo", "Enlace", "Créditos"]

	st.sidebar.image(image, use_column_width=False)

	choice = st.sidebar.selectbox("Seleccione",activites)

	if choice == "Seleccione":
		st.subheader("Seleccione una de las opciones en el menú lateral")

	elif choice == "Subir archivo":

		st.subheader("Sube tu foto en blanco y negro")

		uploaded_file = st.file_uploader("Subir imagen",type=["png","jpg"])
		if uploaded_file is not None:
			st.subheader("Imagen original")
			aaa=uploaded_file.read()
   
			#bytes_data = uploaded_file.getvalue()
			file_bytes = np.asarray(bytearray(aaa), dtype=np.uint8)
			opencv_image = cv2.imdecode(file_bytes, 1)
			st.image(opencv_image, channels="BGR", use_column_width=True)
			#detector = FER(mtcnn=True)

			my_bar = st.progress(0)

			for percent_complete in range(100):
				time.sleep(0.1)
				my_bar.progress(percent_complete + 1)


			r = requests.post(
				"https://api.deepai.org/api/colorizer",
				files={
					'image': file_bytes,
				},
				headers={'api-key': '729dd919-d4f0-4241-8ad1-42e607851be1'}
			)
			st.subheader("Imagen procesada")
			r_json=r.json()

			if str(r) == "<Response [200]>":
				URL_image_out = r_json["output_url"]
				image_out = Image.open(requests.get(URL_image_out, stream=True).raw)		
				st.image(image_out, use_column_width = True)
				st.write("URL imagen procesada: ", URL_image_out)
			else:
				st.write("Error: Intentos máximos alcanzados. Por favor espere un momento para volver a intentar")

	if choice == 'Enlace':
        # https://pbs.twimg.com/profile_images/1069379385847877633/F1YPBji6_400x400.jpg
		st.header("Ingresa la url de la foto")
		input_url = st.text_input("https://pbs.twimg.com/profile_images/1069379385847877633/F1YPBji6_400x400.jpg")
		if input_url != "":
			image = Image.open(requests.get(input_url, stream=True).raw)		
			st.subheader("Imagen original")
			st.image(image, use_column_width = True)

			my_bar = st.progress(0)

			for percent_complete in range(100):
				time.sleep(0.1)
				my_bar.progress(percent_complete + 1)


			r = requests.post(
				"https://api.deepai.org/api/colorizer",
				data={
					'image': input_url,
				},
				headers={'api-key': '729dd919-d4f0-4241-8ad1-42e607851be1'} #729dd919-d4f0-4241-8ad1-42e607851be1 #quickstart-QUdJIGlzIGNvbWluZy4uLi4K
			)
			st.write("URL imagen original: ", input_url)

			st.subheader("Imagen procesada")
			r_json=r.json()
			#st.write(r)

			if str(r) == "<Response [200]>":
				URL_image_out = r_json["output_url"]
				image_out = Image.open(requests.get(URL_image_out, stream=True).raw)		
				st.image(image_out, use_column_width = True)
				st.write("URL imagen procesada: ", URL_image_out)
			else:
				st.write("Error: Intentos máximos alcanzados. Por favor espere un momento para volver a intentar")



	
	elif choice == 'Créditos':
		st.subheader("Créditos")
		st.text("Jorge O. Cifuentes")
		st.write('*jorgecif@gmail.com* :sunglasses:')



if __name__ == "__main__":
    main()