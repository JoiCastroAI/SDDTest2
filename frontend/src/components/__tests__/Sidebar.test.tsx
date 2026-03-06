import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import Sidebar from '../Sidebar';

const renderSidebar = (initialRoute = '/') =>
    render(
        <MemoryRouter initialEntries={[initialRoute]}>
            <Sidebar />
        </MemoryRouter>,
    );

describe('Sidebar', () => {
    it('should render Dashboard and Companies links', () => {
        renderSidebar();
        expect(screen.getByText('Dashboard')).toBeDefined();
        expect(screen.getByText('Companies')).toBeDefined();
    });

    it('should render FastReport logo', () => {
        renderSidebar();
        expect(screen.getByText('FastReport')).toBeDefined();
    });

    it('should highlight active route for Dashboard', () => {
        renderSidebar('/');
        const dashLink = screen.getByText('Dashboard').closest('a');
        expect(dashLink?.className).toContain('active');
    });

    it('should highlight active route for Companies', () => {
        renderSidebar('/companies');
        const compLink = screen.getByText('Companies').closest('a');
        expect(compLink?.className).toContain('active');
    });

    it('should collapse and expand on toggle click', () => {
        renderSidebar();
        const toggle = screen.getByLabelText('Collapse sidebar');
        fireEvent.click(toggle);

        const expandBtn = screen.getByLabelText('Expand sidebar');
        expect(expandBtn).toBeDefined();

        fireEvent.click(expandBtn);
        expect(screen.getByLabelText('Collapse sidebar')).toBeDefined();
    });
});
