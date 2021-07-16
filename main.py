import streamlit as st
import pandas as pd


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Simple Login App"""
	header = st.beta_container()
	dataset = st.beta_container()
	member = st.beta_container()
	with header:
		st.title("Bienvenido/a a LeeMaS")
		st.text('En este proyecto le brindo un resultado de sugerencias de acuerdo al usuario registrado')
	with dataset:
		st.header("Coursera dataset")
		st.subheader('Contenido')
		st.text('Aquí he escarvado datos del sitio web oficial de Coursera. Nuestro proyecto tiene como objetivo ayudar a cualquier alumno nuevo a obtener el curso adecuado para aprender con solo responder algunas preguntas. Es un sistema inteligente de recomendación de cursos. Por lo tanto, tuvimos que eliminar datos de algunos sitios web educativos. Estos son datos excarvados del sitio web de Coursera.')
		st.text('This dataset contains mainly 6 columns and 890 course data. The detailed description:')

# course_title : Contains the course title.
# course_organization : It tells which organization is conducting the courses.
# courseCertificatetype : It has details about what are the different certifications available in courses.
# course_rating : It has the ratings associated with each course.
# course_difficulty : It tells about how difficult or what is the level of the course.
# coursestudentsenrolled : It has the number of students that are enrolled in the course.')
	coursu_data = pd.read_csv('data/complete_course_data.csv')
	st.write(coursu_data.head())
	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:
				with member:
					st.success("Logged In as {}".format(username))
					my_form = st.form(key="form1")
					price = my_form.text_input(label="¿Prefieres cursos gratis, de pago o de cualquier tipo?")
					topic = my_form.text_input(label="¿Tema que quieres tomar en curso?")
					nivel = my_form.selectbox(label="¿Cuál es el nivel de dificultad: todos, principiante, intermedio o avanzado?")#,['todos', 'principiante', 'intermedio', 'avanzado'],key=1)
					platform = my_form.text_input(label="¿Alguna plataforma preferida?")

					# number = my_form.slider("Enter your age", min_value=10, max_value=100)
					submit = my_form.form_submit_button(label="Submit this form")
					task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
					if task == "Add Post":
						st.subheader("Add Your Post")

					elif task == "Analytics":
						st.subheader("Analytics")
					elif task == "Profiles":
						st.subheader("User Profiles")
						user_result = view_all_users()
						clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
						st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()
