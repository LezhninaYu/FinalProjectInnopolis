import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../../context';
import styles from './Header.module.css';
import logo from '../../assets/images/logo.png';

const Header = ({ props }) => {
  const { setIsAuth } = useContext(AuthContext);

  const isLanding = props;

  const handleLogout = () => {
    localStorage.removeItem('isAuth');
    setIsAuth(false);
  };

  return (
    <header className={styles.headerBackground}>
      <Link className={styles.navLogoRef} to='/'>
        <img className={styles.menuLogo} src={logo} alt='Логотип' />
      </Link>
      <nav className={styles.menuNav}>
        <Link  className={styles.landingMenuLink} to='/'>
          Главная
        </Link>
        <Link className={styles.landingMenuLink} to='/posts' >
          Содержание
        </Link>
        <a href='https://github.com/LezhninaYu' className={styles.landingMenuLink}>
          GitHub
        </a>
        {!isLanding && (
          <a
            href='/login'
            onClick={handleLogout}
            className={styles.landingMenuExitLink}>
            Выйти
          </a>
        )}
      </nav>
    </header>
  );
};

export default Header;
