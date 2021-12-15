import React from 'react';
import Header from '../../components/Header/Header';
import { useNavigate } from 'react-router-dom';
import styles from './LandingPage.module.css';
export default function LandingPage() {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate('/posts');
  }
  return (
    <>
      <Header props={true} />
      <section className={styles.section}>
        <div className={styles.form}>
          <h1 className={styles.formTitle}>
            Аттестационная работа <br />
            на React.js
          </h1>

          <button onClick={handleClick} className={styles.startBtn}>Начать!</button>
        </div>
      </section>
    </>
  );
}
