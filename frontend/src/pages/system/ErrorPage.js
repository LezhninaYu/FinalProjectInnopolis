import React from 'react';
import { useLocation } from 'react-router-dom';
import Header from '../../components/Header/Header';
import styles from './ErrorPage.module.css';

export default function ErrorPage() {
    const location = useLocation();
    return (
        <>
            <Header props={true} />
            <section className={styles.section}>
                <h1 className={styles.errorCard}>Страница {location.pathname} не найдена.</h1>
            </section>
        </>
    );
}
