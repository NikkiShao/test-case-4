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
  const forestLink = screen.getByText(/Forest/i);
  expect(forestLink).toBeInTheDocument();
  const fieldLink = screen.getByText(/Field/i);
  expect(fieldLink).toBeInTheDocument();
  const seaLink = screen.getByText(/Sea/i);
  expect(seaLink).toBeInTheDocument();
});
