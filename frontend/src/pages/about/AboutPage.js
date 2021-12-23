import React from 'react';
import Header from '../../components/Header/Header';
import { useNavigate } from 'react-router-dom';
import styles from './AboutPage.module.css';
import QRcode from '../../assets/images/QRcode.png';

export default function AboutPage() {
  const navigate = useNavigate();
  return (
    <>
      <Header props={true} />
      <section className={styles.section}>
        <div className={styles.form}>
          <h1 className={styles.formTitle}>
            Приложение содежит карточки с информацией<br />
            о студентах
          </h1>
          <img className={styles.QRimage} src={QRcode} alt='QR-код' />
        </div>
      </section>
    </>
  );
}
