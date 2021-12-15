import React, { useContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Header from '../../components/Header/Header';
import { AuthContext } from '../../context';
import styles from './AuthPage.module.css';
import API from '../../api';

export default function AuthPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { isAuth, setisAuth } = useContext(AuthContext);
  const navigate = useNavigate();

  if (isAuth) {
    navigate('/posts');
  }

  const handleEmailChange = e => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = e => {
    setPassword(e.target.value);
  };

  const handleLogin = async e => {
    e.preventDefault();

    e.preventDefault();

    const authData = {
      email: email,
      password: password,
    };

    const authReponse = await API.post(`/users/login`, authData);
    console.log(authReponse)
    if (authReponse.status === 200) {
      localStorage.setItem('isAuth', 'true');
      setisAuth(true);
      alert("Successful login");
      navigate('/posts');
    }
    else if (authReponse.status === 404) {
      alert("User not found");
    }
    else if (authReponse.status === 400) {
      alert("Bad credentials");
    }

  };

  return (
    <>
      <Header props={true} />
      <section className={styles.section}>
        <form className={styles.form}>
          <h1 className={styles.formTitle}>Логин</h1>
          <div className={styles.inputContainer}>
            <label className={styles.inputLabel}>Почта</label>
            <input className={styles.input} onChange={handleEmailChange} type='text' />
          </div>
          <div className={styles.inputContainer}>
            <label className={styles.inputLabel}>Пароль</label>
            <input className={styles.input} onChange={handlePasswordChange} type='password' />
          </div>
          <button className={styles.loginBtn} onClick={handleLogin}>
            Войти
          </button>
        </form>
      </section>
    </>
  );
}
