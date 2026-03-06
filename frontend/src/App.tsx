import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import AppLayout from './components/AppLayout';
import DashboardPage from './pages/DashboardPage';
import CompaniesPage from './pages/CompaniesPage';

const App: React.FC = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route element={<AppLayout />}>
                    <Route path="/" element={<DashboardPage />} />
                    <Route path="/companies" element={<CompaniesPage />} />
                </Route>
            </Routes>
        </BrowserRouter>
    );
};

export default App;
