import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import App from './App';

test('renders navigation links', () => {
  render(
    <BrowserRouter>
      <App />
    </BrowserRouter>
  );
  const homeLink = screen.getByText(/Home/i);
  expect(homeLink).toBeInTheDocument();
  const aboutLink = screen.getByText(/About/i);
  expect(aboutLink).toBeInTheDocument();
  const contactLink = screen.getByText(/Contact/i);
  expect(contactLink).toBeInTheDocument();
});
